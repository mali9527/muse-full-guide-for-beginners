"""Case links must survive combining chapters, without changing code examples."""
import sys
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from studio_lib.builder import rewritten_body


class CaseAnchorTests(unittest.TestCase):
    def test_case_targets_and_literal_examples(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            units = [{"id": name, "path": name + ".md"} for name in ("one", "two")]
            text = '# Chapter\n\n<a id="c01"></a>\n\n[Here](#c01) [There](two.md#c01)\n'
            code = '`<a id="inline"></a>`\n\n```html\n<a id="fenced"></a>\n```\n'
            for unit in units:
                (root / unit["path"]).write_text(text + code)
            for pdf_mode in (False, True):
                with self.subTest(pdf_mode=pdf_mode):
                    result = rewritten_body(root, units[0], text + code, root, units, pdf_mode=pdf_mode)
                    self.assertIn('[Here](#one-c01) [There](#two-c01)', result)
                    self.assertIn('#metadata("one-c01") #label("one-c01")' if pdf_mode else '<a id="one-c01"></a>', result)
                    other = rewritten_body(root, units[1], text, root, units, pdf_mode=pdf_mode)
                    self.assertIn('#metadata("two-c01") #label("two-c01")' if pdf_mode else '<a id="two-c01"></a>', other)
                    self.assertIn(code.rstrip("\n"), result)

    @unittest.skipUnless(shutil.which("pandoc") and shutil.which("typst"), "PDF tools required")
    def test_adjacent_aliases_compile_to_distinct_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            unit = {"id": "one", "path": "one.md"}
            text = '# Chapter\n\nPrevious paragraph.\n\n<a id="c03"></a>\n<a id="c04"></a>\n\n## Combined case\n\n[First](#c03) [Alias](#c04)\n'
            (root / "one.md").write_text(text)
            rendered = rewritten_body(root, unit, text, root, [unit], pdf_mode=True)
            (root / "export.md").write_text(rendered)
            subprocess.run(["pandoc", "export.md", "--to=typst", "--standalone", "-o", "book.typ"], cwd=root, check=True, capture_output=True)
            result = subprocess.run(["typst", "compile", "book.typ", "book.pdf"], cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn("labelled multiple times", result.stderr)


if __name__ == "__main__":
    unittest.main()
