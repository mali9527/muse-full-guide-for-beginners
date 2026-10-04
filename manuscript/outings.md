# 第 16 章 旅行与出门：行程、票务、餐厅和出门前的信息

<!-- studio:nav -->
← [第 15 章 家庭生活：日程、资料、家务和孩子的事](household.md) · [目录](../README.md) · [第 17 章 购物与消费：找货、比价、取消服务和询价](shopping.md) →
<!-- /studio:nav -->

出门的事分两段：出门前要把信息找齐，订票订位要和各家网站打交道。本章既有从邮件找齐资料的经历，也有订票时被登录、验证码和网站规则拦住的经历。

值得先看三条。一位记者临出门记不清演讲地点和停车，连联系人名字都拼错了，Muse 从旧邮件里把地点、停车、电话和地图找齐了（[C43](#c43)）。另一位记者让它给朋友发邮件问旅行想法，收到回复后整理成一份文档（[C07](#c07)）。订机票的两次经历放在一起看：Engadget 的记者拿到了只要直飞的选项和一个价格追踪（[C61](#c61)），Slate 的记者卡在验证码上，三十分钟一无所获（[C62](#c62)）。

## 案例

<a id="c43"></a>

### C43 临出门，从旧邮件里找齐演讲地点、停车和联系人

媒体实测 · TechRadar · Lance Ulanoff · 2026-09-28

**事情。** 他要去做一场演讲，记不清地点和停车安排，联系人的名字还拼错了。

**过程与结果。** 他只给了 Muse 联系人的名字（拼错的）和所在城镇，Muse 找到了原来的邀请邮件，整理出地点、停车信息、联系人电话，还附了一张地图。他之后又让它调出原邀请核对。

原文：

> location, parking, my contact's phone number

译文：地点、停车信息、我联系人的电话号码。

出处：[I gave Muse access to my personal data and now I know why personal agents are probably going to change the world（TechRadar）](https://www.techradar.com/ai-platforms-assistants/i-gave-muse-access-to-my-personal-data-and-now-i-know-why-personal-agents-are-probably-going-to-change-the-world)，「Muse knew less about me than I thought」一节。本书读取：2026-10-01、2026-10-04。

提醒：要先接入邮箱。它能从旧邮件里找，不是凭空知道。

<a id="c07"></a>

### C07 让它先问朋友的想法，再把回复整理成一份行程文档

媒体实测 · CNN · Lisa Eadicicco · 2026-09-23

**事情。** 下个月要和朋友去新泽西的 Cape May，想知道朋友的打算。

**过程与结果。** 她接入 Google 应用后，让 Muse 给朋友发邮件问想法。朋友回复后，她让 Muse 把朋友推荐的餐厅整理成一份 Google 文档，还补上了类似的备选。事情到文档为止，没有写预订。

原文：

> package her restaurant recommendations into a polished Google Doc

译文：把她推荐的餐厅整理成一份清楚的 Google 文档。

出处：[Meta says its Muse AI agent can do things for you. I put it to the test（CNN，经 KESQ 转载）](https://kesq.com/money/cnn-business-consumer/2026/09/23/meta-says-its-muse-ai-agent-can-do-things-for-you-i-put-it-to-the-test/)。本书读取：2026-09-30、2026-10-04。

提醒：发邮件之前，检查收件人和内容，再决定自行发送或授权发送。

<a id="c61"></a>

### C61 只要直飞的航班，它给了几个选项，还设了价格追踪

媒体实测 · Engadget · Karissa Bell · 2026-09-12

**事情。** 她在计划一次可能跨几个城市的旅行。

**过程与结果。** 她给了时间和偏好（只要直飞），Muse 给出从她所在城市出发的几个航班选项，并设了一个价格追踪。它还建议了城市的先后顺序，并提议考虑多城市联程票，这样可以从另一个机场回来。

原文短引：

> set up a price tracker to monitor the cost.

译文：设置了价格追踪，监测费用。

出处：[How to get started with Meta's new AI agent, Muse（Engadget）](https://www.engadget.com/2256577/how-to-get-started-with-meta-s-new-ai-agent-muse/)，文末旅行段。本书读取：2026-10-04。

提醒：到选项和追踪为止，没有订票。

<a id="c37"></a>

### C37 每天同时盯机票和租车，等到符合自己的条件

网友分享 · Reddit r/MetaAI · SeatownCooks · 发表日期未确认

**事情。** 他每年同一时间去佛罗里达。

**过程与结果。** 他让 Muse 每天查机票和租车价格，直到找到符合要求、价格也合适的选项。帖子没说这次订到没有、省了多少。

原文：

> Daily travel search. I go to Florida every year at the same time. I have it scanning daily for airfare and rental car prices until it finds my specifications at the price I want.

译文：每日旅行搜索。我每年同一时间去佛罗里达。我让它每天扫描机票和租车价格，直到找到符合我要求、价格也合我意的。

出处：[How do I get the most use out of Muse?（Reddit r/MetaAI）](https://www.reddit.com/r/MetaAI/comments/1wozi3y/how_do_i_get_the_most_use_out_of_muse/) 的评论。本书读取：2026-10-01、2026-10-04。

提醒：这是周期任务，监测会持续消耗额度。

<a id="c62"></a>

### C62 订机票卡在验证码上，三十分钟一无所获

媒体实测 · Slate · Alex Kirshner · 2026-09-23

**事情。** 他想让 Muse 替他订一张机票。

**过程与结果。** 他把航空公司的登录信息放进 Muse 的保险库，Muse 到登录页就撞上了验证码。它失败了，他接手登录，再把控制权交回去，几分钟后它又被踢出浏览器。他写道，整个过程三十分钟，什么也没办成。文章里还有一件事：他让 Muse 在日历上加一个「明天上午十点」的事件，它加到了过去的时间（见第 18 章 [C88](office.md#c88)）。

出处：[Slate 的 Muse 评测](https://slate.com/technology/2026/09/meta-muse-ai-app-review.html)。本书读取：2026-10-04。作者在 [Bluesky 的帖子](https://bsky.app/profile/alexkirshner.com/post/3mw7frxezq22a)里也说了「三十分钟、失败」。

提醒：这次经历里，作者接手验证后仍没能完成订票。遇到反复验证或掉线，可以直接接手完成，不必一直重试。

<a id="c63"></a>

### C63 查去拉斯维加斯的航班，建了每日监价，最后还是自己查

创作者分享 · Substack（The Automated Operator） · Alex Willen · 2026-09-22

**事情。** 他要去拉斯维加斯，想让 Muse 查指定航空公司的航班并盯价格。

**过程与结果。** 指定 JSX 航班的查价和每日监控建成了。返程的推荐和用积分的方案他不满意。英国航空的网站出现验证码，他提示后 Muse 过了，接着航班搜索页报错。他最后放弃，自己去查，发现没有可订的航班。

原文：

> Finally, I gave up and looked myself: no flights available.

译文：最后我放弃了，自己去查：没有可订的航班。

出处：[Meta's Muse is surprisingly unimpressive（The Automated Operator）](https://theautomatedoperator.substack.com/p/metas-muse-is-surprisingly-unimpressive)。本书读取：2026-10-04。

提醒：作者整篇的评价偏负面。这件事里，查价和监控建成了，订票没成，两段要分开看。

<a id="c64"></a>

### C64 找供应无麸质啤酒的餐厅，它推荐了一家关了几年的店，还编了一个电话

媒体实测 · Yahoo Finance · Daniel Howley · 2026-09-23 前后

**事情。** 他想找附近供应无麸质啤酒的餐厅。

**过程与结果。** Muse 给了两个对的，另一个是已经关门多年的店。他指出后，Muse 道歉，说一开始用了过时的数据。他又问一家他知道有这种啤酒的店，Muse 说店的网站上没写，建议他打电话问。电话号码这件事更离谱：Muse 先给了一个号，又说换一个，他问为什么，Muse 承认第一个号是凭空编的，没有核实，还叮嘱他不要相信它给出的未经核实的号码。

出处：[Meta's Muse is an impressively capable AI agent, despite some hiccups（Yahoo Finance）](https://finance.yahoo.com/technology/article/metas-muse-is-an-impressively-capable-ai-agent-despite-some-hiccups-173310662.html)。本书读取：2026-10-04。作者的 [LinkedIn 帖](https://www.linkedin.com/posts/daniel-howley-0b117712_metas-muse-is-an-impressively-capable-ai-activity-7508599611520098305-woJg)也提到编号码这件事。

提醒：打电话或出发前，用商家自己的页面确认电话、地址和营业状态。

<a id="c65"></a>

### C65 订一顿约会晚餐，四个建议里挑一个，通过 OpenTable 订了

媒体实测 · Yahoo Finance · Daniel Howley · 2026-09-23 前后

**过程与结果。** 他给了 Muse 一些基本想法，Muse 回了四个建议，他挑了一家，通过 Muse 在 OpenTable 上订了位。

出处：[Meta's Muse is an impressively capable AI agent, despite some hiccups（Yahoo Finance）](https://finance.yahoo.com/technology/article/metas-muse-is-an-impressively-capable-ai-agent-despite-some-hiccups-173310662.html)。本书读取：2026-10-04。

提醒：同一位记者，同一篇文章，[C64](#c64) 是翻车，[C65](#c65) 是成功。

<a id="c66"></a>

### C66 要约会地点的清单，两家已经关门多年

媒体实测 · CNN · Lisa Eadicicco · 2026-09-23

**过程与结果。** 她要一份约会可去的地方清单，Muse 列出的两家本地店已经关门好几年了。文章开头说她订好了周五的约会晚餐，但没写完整的订位过程。

原文短引：

> had been closed for years.

译文：已经关门好几年了。

出处：[CNN 的实测（经 KESQ 转载）](https://kesq.com/money/cnn-business-consumer/2026/09/23/meta-says-its-muse-ai-agent-can-do-things-for-you-i-put-it-to-the-test/)，「Things that were easier to do on my own」一节。本书读取：2026-10-04。

提醒：和 [C64](#c64) 是不同记者的相同遭遇。

<a id="c67"></a>

### C67 订餐厅没订成，推荐的电影也没看

媒体实测 · The New Yorker · Brady Brickner-Wood · 2026-09-16

**过程与结果。** 他让 Muse（他起名 Harbor）订一顿晚餐，Muse 转到 Resy 网站后遇到登录和验证障碍，他自己订了；后来全家还是错过了那次预约。预约失败后他让 Muse 推荐一部晚上看的电影，Muse 给了建议，他们没看。同一篇文章里成功的那件事在第 22 章（[C114](business.md#c114)）。

出处：[My Weekend with an A.I. Agent（The New Yorker）](https://www.newyorker.com/culture/infinite-scroll/my-weekend-with-an-ai-agent)。本书读取：2026-10-04。

提醒：推荐和预订分开核对：有推荐，不等于已经订好；自己完成预约后也要留意时间。

<a id="c68"></a>

### C68 让它在餐厅开放预订的那一刻打电话抢位，他说六成成功

网友分享 · Reddit r/MetaAI · DesignSpartan · 发表日期未确认 · 需要测试资格

**过程与结果。** 他说 Resy、OpenTable 有时抢不到位，他让 Muse 在餐厅开放预订时打电话去订，连 Amex 礼宾都订不到的位也试过。他自报六成有效。他说打电话是早期测试功能，要向 Muse 申请加入。

原文：

> Restaurant reservations. using the call feature. Sometimes resy or OpenTable suck so I basically tell it to call right at open to try and secure reservations that I otherwise can’t even get with Amex concierge. 60% effective. Not bad! This is an early access feature. Just ask Muse to sign you up for the outbound call beta, and you might get in.

译文：餐厅订位。用打电话功能。有时候 Resy 或 OpenTable 不好使，我就让它在开放预订时打电话去抢，连用 Amex 礼宾都订不到的位也试。六成有效。不错！这是早期测试功能，让 Muse 给你报名外呼测试，可能就能进。

出处：[Top three use cases for Muse（Reddit r/MetaAI）](https://www.reddit.com/r/MetaAI/comments/1wrwwx2/top_three_use_cases_for_muse/?sort=confidence) 的评论。本书读取：2026-10-04。

提醒：打电话功能不是所有账号都有，其他评论者说自己没有。「六成」是他自己的说法，没有样本。主帖含推荐码。

<a id="c69"></a>

### C69 它发现租车取车时间和航班到达对不上，自己改了预约

网友分享 · Reddit r/MetaAI · Bluehens96 · 2026-10-02

**过程与结果。** Muse 主动发现他的租车取车时间和航班到达时间不一致，在邮件里找到修改预约的链接，替他改了。他说这救了他。帖子没说改的时候有没有逐步确认、有没有产生费用。

原文：

> He proactively noticed that my rental car pick up time does not match my flight arrival time. Checked for the modification link in my email and updated my reservation for me (lifesaver)

译文：它主动注意到我的租车取车时间和航班到达时间对不上。在我的邮件里找到修改链接，替我改了预约（救命了）。

出处：[Top three use cases for Muse（Reddit r/MetaAI）](https://www.reddit.com/r/MetaAI/comments/1wrwwx2/top_three_use_cases_for_muse/?sort=confidence)。本书读取：2026-10-04。

提醒：这是「主动替你改」，不是「主动提醒你」。你需要先明确是否允许它直接修改预约，并检查已有许可。

<a id="c70"></a>

### C70 让它读完 Letterboxd 片单，推荐一部电影

网友分享 · Reddit r/MetaAI · SignificantEgg6253 · 发表日期未确认

**过程与结果。** 他让 Muse 看他的 Letterboxd 待看清单，推荐一部电影，他说电影挺好。他解释了过程：Muse 本来一部一部地去看，他发现 Letterboxd 每部电影有一个输出纯数据的网址，就让 Muse 写个小脚本批量取，然后再做决定。

原文：

> Lastly, got it to look through my Letterboxd watchlist and recommend me a movie to watch. Pretty good movie.

译文：最后，让它翻我的 Letterboxd 待看清单，给我推荐一部电影。电影挺不错。

出处：[Top three use cases for Muse（Reddit r/MetaAI）](https://www.reddit.com/r/MetaAI/comments/1wrwwx2/top_three_use_cases_for_muse/?sort=confidence) 的帖子，另一位评论者。本书读取：2026-10-04。

提醒：他中途介入，让 Muse 换了取数据的方法。评论含推荐码。

<a id="c27"></a>

### C27 找好 IMAX 场次，一路走到结账页

创作者分享 · ChatPRD · Claire Vo · 2026-09-16

**事情。** 她想看《The Odyssey》的 IMAX 版，Daly City 这周的白天场。

**过程与结果。** 她让 Muse 查场次，回答了它关于票数的提问，然后看着它进入影院网站的访客结账流程，付款那一步出现了 Stripe Link。她没有买，三小时的电影她现在没时间看。她说这个流程顺畅，比之前买鞋的经历好得多（买鞋见第 17 章 [C72](shopping.md#c72)）。

原文：

> While I didn't actually buy the tickets

译文：虽然我并没有真的买票。

出处：[Claire Vo 的文字实录（ChatPRD）](https://www.chatprd.ai/how-i-ai/meta-muse-review-personal-ai-agent)，「Test 2: Buying IMAX Tickets」一节。本书读取：2026-10-01、2026-10-04。

提醒：到结账为止，没有付款。节目有赞助商，不是 Meta。

<a id="c06"></a>

### C06 让它定期留意家附近有没有新开的餐厅

网友分享 · Reddit r/MetaAI · CaptainBroccoli · 发表日期未确认

**过程与结果。** 他让 Muse 定期上网查，有新餐厅开业就告诉他，因为他们喜欢支持本地新店。帖子没有给出具体餐厅或通知的样子。有评论者质疑：产品才出来几天，哪有那么多新开的餐厅可以追踪。

原文：

> New Restaurants in My Neighborhood - Not as exciting, but Muse checks the web for me periodically and tells me if there are any new restaurants opening up around me. We always like to support new local businesses!

译文：我家附近的新餐厅。没那么刺激，但 Muse 会定期替我上网查，告诉我附近有没有新开的餐厅。我们一直喜欢支持本地新店！

出处：[Useful things I've set up with Muse（Reddit r/MetaAI）](https://www.reddit.com/r/MetaAI/comments/1wk92xe/useful_things_ive_set_up_with_muse/)。本书读取：2026-09-30、2026-10-04。

提醒：主帖含推荐码。[C64](#c64)、[C66](#c66) 说明餐厅信息可能过时，收到通知后自己核一下。

## 线索

- 让 Muse 跑了 146 次机票搜索，从旧金山到十一个西班牙城市去、十个意大利城市回，跨七个日期，找最便宜的往返。[Deep Mehta 在 X 上的原帖](https://x.com/mehtadeep/status/2099498596789850192)，[聚合站的转述](https://shipwithmuse.live/builds/146-flight-searches-for-the-cheapest-europe-trip)。本书没打开原帖，搜索次数和省钱数字都没核。
- 航班延误七小时后让 Muse 申请补偿，自述拿到替代航班和 250 美元的 Delta 额度。Tom's Guide 的[十个用法整理](https://www.tomsguide.com/ai/i-scoured-reddit-for-muse-ai-use-cases-10-that-will-actually-save-you-time)转述自 [X 上的帖子](https://x.com/cryptopunk7213/status/2102179999122153690)，本书没打开原帖。额度不是现金。

## 换成自己的事

出门前找信息，可以参考 [C43](#c43)：说清是哪件事、大概什么时候、涉及谁，并确认 Muse 能访问相关邮件。找到之后，打开原邮件核对地点、日期和联系人，尤其留意后来的变更。

订票订位要分三段看：找到候选，提交，对方确认。[C61](#c61)、[C37](#c37) 停在找到候选，[C65](#c65) 走完了三段，[C62](#c62)、[C67](#c67) 卡在提交那一步。

餐厅信息过时是反复出现的问题（[C64](#c64)、[C66](#c66)）。出发前用商家当前页面核对地址、营业状态和电话。

[C69](#c69) 那种它自己发现问题、自己改预约的事，省心，也要紧。改预约可能产生费用。你希望它遇到这种事先问你，还是直接办，要在交办时说明，并检查相应的许可设置。
