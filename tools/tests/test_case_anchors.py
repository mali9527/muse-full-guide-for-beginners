"""Case links must survive combining chapters, without changing code examples."""
import sys
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
                    self.assertIn('[]{#one-c01}' if pdf_mode else '<a id="one-c01"></a>', result)
                    other = rewritten_body(root, units[1], text, root, units, pdf_mode=pdf_mode)
                    self.assertIn('[]{#two-c01}' if pdf_mode else '<a id="two-c01"></a>', other)
                    self.assertIn(code.rstrip("\n"), result)


if __name__ == "__main__":
    unittest.main()
