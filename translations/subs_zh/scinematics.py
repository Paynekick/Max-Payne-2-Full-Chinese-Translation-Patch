# -*- coding: utf-8 -*-
"""cinematics.h 过场字幕全量翻译 (方案B: 写回 .ras, 按 ID 匹配)"""

SUBS = {
    # --- Cinematic 010 ---
    # 英文: God!
    "Cinematic_010_01": "天啊！",
    # 英文: I turned out to be such a damsel in distress.
    "Cinematic_010_02": "到头来，我竟成了需要被拯救的落难少女。",
    # 英文: They were all dead.
    "Cinematic_010_03": "他们全都死了。",
    # 英文: Love kills.
    "Cinematic_010_04": "爱会杀人。",
    # 英文: Did I love her?
    "Cinematic_010_05": "我当时爱她吗？",
    # 英文: Was there a choice?
    "Cinematic_010_06": "我有选择吗？",
    # 英文: The past is a gaping hole.
    "Cinematic_010_07": "过去是一道口子大开的深渊。",
    # 英文: You try to run from it,
    "Cinematic_010_08": "你试图逃离它，",
    # 英文: but the more you run, the deeper,
    "Cinematic_010_09": "可你跑得越远，它就越深，",
    # 英文: more terrible it grows behind you,
    "Cinematic_010_10": "在你身后生长得越发可怖，",
    # 英文: its edges yawning at your heels.
    "Cinematic_010_11": "它的边缘在你脚后跟处张着大口。",

    # --- Cinematic 020 ---
    # 英文: Max.
    "Cinematic_020_01": "马克思。",
    # 英文: Max, dearest of all my friends.
    "Cinematic_020_02": "马克思，我最亲爱的朋友。",
    # 英文: Payne?
    "Cinematic_020_03": "佩恩？",
    # 英文: It's yours, Payne.
    "Cinematic_020_04": "这是你的了，佩恩。",
    # 英文: You're the man.
    "Cinematic_020_05": "你真行。",
    # 英文: Max! 911!
    "Cinematic_020_06": "马克思！911！",
    # 英文: Max, sorry I woke you.
    "Cinematic_020_07": "马克思，抱歉吵醒你。",
    # 英文: Run, Payne, run!
    "Cinematic_020_08": "跑啊，佩恩，快跑！",

    # --- Cinematic 030 ---
    # 英文: What are you so afraid of?
    "Cinematic_030_01": "你到底在怕什么？",
    # 英文: What do you want from me?
    "Cinematic_030_02": "你到底想从我这儿得到什么？",

    # --- Cinematic 035 ---
    # 英文: Found him.
    "Cinematic_035_01": "找到他了。",
    # 英文: Freeze! NYPD!
    "Cinematic_035_02": "别动！纽约警局！",

    # --- Cinematic 040 ---
    # 英文: She's one of them. She's here to kill me.
    "Cinematic_040_01": "她是他们的人。她是来杀我的。",
    # 英文: Back off, Payne.
    "Cinematic_040_02": "退后，佩恩。",
    # 英文: Winterson!
    "Cinematic_040_03": "温特森！",

    # --- Cinematic 060 ---
    # 英文: Payne!
    "Cinematic_060_01": "佩恩！",
    # 英文: You're not going anywhere.
    "Cinematic_060_02": "你哪儿也别想去。",
    # 英文: What happened out there? You did it.
    "Cinematic_060_03": "外面到底发生了什么？是你干的！",
    # 英文: Internal Affairs is breathing down my neck.
    "Cinematic_060_04": "内务部正掐着我的脖子不放。",
    # 英文: Did you do it? You killed her.
    "Cinematic_060_05": "到底是不是你干的？你杀了她。",
    # 英文: No. I can't -
    "Cinematic_060_06": "不。我也没办法——",
    # 英文: Bullshit!
    "Cinematic_060_07": "该死！",

    # --- Cinematic 080 ---
    # 英文: Help! No, stay back! Get away from me! Help!
    "Cinematic_080_06": "救命！不，退后！离我远点！救命！",
    # 英文: I need backup. Unknown number of armed perps inside.
    "Cinematic_080_07": "我需要支援。楼内有数量不明的武装嫌犯。",
    # 英文: Possible hostage situation.
    "Cinematic_080_08": "可能有挟持人质的情况。",
    # 英文: Ten four. Backup is on its way.
    "Cinematic_080_09": "收到。支援正在赶来。",
    # 英文: I'm going in.
    "Cinematic_080_10": "我要进去了。",

    # --- Cinematic 110 ---
    # 英文: NYPD!
    "Cinematic_110_01": "纽约警局！",
    # 英文: Woah, easy officer, easy. Just cleaning the place.
    "Cinematic_110_02": "哇，警官，冷静，冷静。只是在打扫这地方。",
    # 英文: C'mon officer. It's all legit.
    "Cinematic_110_03": "拜托了警官，一切都是合法的。",
    # 英文: I work for the Squeaky Cleaning Company.
    "Cinematic_110_04": "我为吱吱清洁公司干活。",
    # 英文: You didn't hear anything suspicious just now?
    "Cinematic_110_05": "你刚没听到什么可疑的动静？",
    # 英文: No, no. Oh, wait.
    "Cinematic_110_06": "没有，没有。哦，等等。",
    # 英文: You mean the gun workshop upstairs?
    "Cinematic_110_07": "你是说楼上的军火作坊？",
    # 英文: Take me there. Move.
    "Cinematic_110_08": "带我去那儿。快。",
    # 英文: Sure, officer. If that's what you want.
    "Cinematic_110_09": "当然，警官。如果您要这样。",

    # --- Cinematic 130 ---
    # 英文: Enough chit-chat. Finish her.
    "Cinematic_130_01": "闲聊够了。干掉她。",
    # 英文: Wait! The mob guys attacked us. I have no beef with you guys.
    "Cinematic_130_02": "等等！是黑帮的人袭击了我们。我和你们无冤无仇。",
    # 英文: You took them out. Listen, I work for Vladimir -
    "Cinematic_130_03": "你把他们都干掉了。听我说，我替弗拉德干活——",
    # 英文: Honey, you work for no one.
    "Cinematic_130_04": "宝贝，你谁也不替。",
    # 英文: What do you want? We.. we can -
    "Cinematic_130_05": "你们想要什么？我们……我们可以——",
    # 英文: NYPD! Drop 'em!
    "Cinematic_130_06": "纽约警局！把枪放下！",
    # 英文: Finish her!
    "Cinematic_130_07": "干掉她！",
    # 英文: Oh God! No!
    "Cinematic_130_08": "哦天啊！不！",
    # 英文: Like all the bad things in my life,
    "Cinematic_130_09": "就像我人生中所有糟糕的事一样，",
    # 英文: it started with a death of a woman.
    "Cinematic_130_10": "都始于一个女人的死亡。",
    # 英文: I couldn’t save her.
    "Cinematic_130_11": "我没能救下她。",

    # --- Cinematic 135 ---
    # 英文: Come on, come on!
    "Cinematic_135_01": "快点，快点！",
    # 英文: Finally.
    "Cinematic_135_02": "终于。",
    # 英文: Hey!
    "Cinematic_135_03": "嘿！",
    # 英文: Mona?
    "Cinematic_135_04": "莫娜？",
    # 英文: Max, we gotta stop meeting like this.
    "Cinematic_135_05": "马克思，我们真不能再这样见面了。",

    # --- Cinematic 140 ---
    # 英文: Get in! Go, Kaufman, go!
    "Cinematic_140_01": "上车！走，考夫曼，快走！",
    # 英文: Max!
    "Cinematic_140_02": "马克思！",
    # 英文: You all right?
    "Cinematic_140_03": "你没事吧？",
    # 英文: I'm okay. Damn it.
    "Cinematic_140_04": "我没事。该死。",
    # 英文: Hey, we're working together on this.
    "Cinematic_140_05": "嘿，我们是同事啊。",

    # --- Cinematic 150 ---
    # 英文: Vlad!
    "Cinematic_150_01": "弗拉德！",
    # 英文: Max! 911! Bad guys with big guns!
    "Cinematic_150_02": "马克思！911！拿着大枪的坏蛋！",
    # 英文: They've got me pinned down in the entrance hall.
    "Cinematic_150_03": "他们把我压制在大厅入口动弹不得。",
    # 英文: Could use some help, could use it now!
    "Cinematic_150_04": "需要支援，现在就要！",
    # 英文: I had to find another way to reach Vlad.
    "Cinematic_150_05": "我得另寻办法去够到弗拉德。",
    # 英文: No time to call backup.
    "Cinematic_150_06": "没时间呼叫支援了。",
    # 英文: My case had a life of its own.
    "Cinematic_150_07": "我的案子有了自己的生命，自行发展下去。",
    # 英文: I got in through the back door.
    "Cinematic_150_08": "我从后门进来的。",

    # --- Cinematic 160 ---
    # 英文: Die Russian! Fucking die already!
    "Cinematic_160_01": "去死吧俄国佬！他妈的赶紧死！",
    # 英文: You are not even trying!
    "Cinematic_160_02": "你根本就没在卖力！",
    # 英文: Hang on, Vlad!
    "Cinematic_160_03": "撑住，弗拉德！",
    # 英文: I'm coming!
    "Cinematic_160_04": "我来了！",
    # 英文: Max!
    "Cinematic_160_05": "马克思！",
    # 英文: Ow no! Payne! Not him! Fuck! Fuck! Fuck!
    "Cinematic_160_06": "噢不！佩恩！别是他！操！操！操！",
    # 英文: What are you waiting for? Circle around and kill him!
    "Cinematic_160_07": "你还在等什么？绕过去干掉他！",
    # 英文: Kill the cop!
    "Cinematic_160_08": "杀了那个警察！",

    # --- Cinematic 170 ---
    # 英文: Payne!
    "Cinematic_170_01": "佩恩！",
    # 英文: You'll fucking pay for this, Russian, you'll fucking pay!
    "Cinematic_170_02": "你他妈会付出代价的，俄国佬，你他妈会付出代价的！",
    # 英文: My hero!
    "Cinematic_170_03": "我的英雄！",
    # 英文: You saved my life. I could kiss you.
    "Cinematic_170_04": "你救了我的命。我真想吻你。",

    # --- Cinematic 190 ---
    # 英文: You don’t need a lawyer. Just tell us what you did.
    "Cinematic_190_01": "你不需要律师。老实交代你干了什么。",
    # 英文: Payne, you’re done!
    "Cinematic_190_02": "佩恩，你完了！",
    # 英文: Everything you say will be used against you.
    "Cinematic_190_03": "你所说的一切都将作为对你不利的证据。",
    # 英文: What are you hiding? She is alive, isn’t she?
    "Cinematic_190_04": "你在隐瞒什么？她还活着，不是吗？",
    # 英文: People get near you, they die.
    "Cinematic_190_05": "谁靠近你，谁就死。",
    # 英文: You killed your family. You killed them all.
    "Cinematic_190_06": "你杀了自己的家人。你把他们都杀了。",
    # 英文: Confess.
    "Cinematic_190_07": "认罪吧。",
    # 英文: Do I get my phone call?
    "Cinematic_190_08": "我能打个电话吗？",
    # 英文: You already got it.
    "Cinematic_190_09": "你已经打过了。",

    # --- Cinematic 210 ---
    # 英文: The real thing is never what you think it will be.
    "Cinematic_210_01": "真实的东西，从来都不是你想的那样。",
    # 英文: Sniper!
    "Cinematic_210_02": "狙击手！",
    # 英文: They’ve found me.
    "Cinematic_210_03": "他们找到我了。",
    # 英文: This was a mistake.
    "Cinematic_210_04": "这是个错误。",
    # 英文: Wait. Mona!
    "Cinematic_210_05": "等等。莫娜！",

    # --- Cinematic 240 ---
    # 英文: ... it's a late goodbye ...
    "Cinematic_240_01": "…这是迟来的告别…",
    # 英文: Hey, hey!
    "Cinematic_240_02": "嘿，嘿！",
    # 英文: NYPD.
    "Cinematic_240_03": "纽约警局。",
    # 英文: I need the code to the 7th floor door.
    "Cinematic_240_04": "我需要七楼门禁的密码。",
    # 英文: Sure, sure. I know it, I know it. Wait. -
    "Cinematic_240_05": "知道，知道。我知道，我知道。等等。——",
    # 英文: Oh yeah. Six six seven, the neighbor of the beast. Get it?
    "Cinematic_240_06": "哦对。六六七，野兽的邻居。懂吗？",
    # 英文: Yeah, I get it.
    "Cinematic_240_07": "嗯，我懂。",

    # --- Cinematic 250 ---
    # 英文: Thanks, you’re a real nice guy.
    "Cinematic_250_01": "谢了，你真是个好人。",
    # 英文: Her kiss made me think of Mona,
    "Cinematic_250_02": "她的吻让我想起了莫娜，",
    # 英文: and that made me uneasy.
    "Cinematic_250_03": "而这让我不安。",

    # --- Cinematic 320 ---
    # 英文: I’ll tell one thing, Mona, you’re no singer.
    "Cinematic_320_01": "我说一句，莫娜，你可不是当歌手的料。",
    # 英文: You’ve switched tactics.
    "Cinematic_320_02": "你换战术了。",
    # 英文: We need to talk.
    "Cinematic_320_03": "我们需要谈谈。",
    # 英文: Bring me a towel, will you.
    "Cinematic_320_04": "给我拿条毛巾，行吗。",
    # 英文: Now that you are here,
    "Cinematic_320_05": "既然你来了，",
    # 英文: you can watch my back while I get dressed.
    "Cinematic_320_06": "我换衣服时，你帮我看着背后。",
    # 英文: All she had told me was that someone wanted us dead.
    "Cinematic_320_07": "她只告诉我一件事——有人想置我们于死地。",
    # 英文: The way she was acting, I was the only one in danger here.
    "Cinematic_320_08": "看她那副做派，好像这里只有我一个人处境危险。",

    # --- Cinematic 330 ---
    # 英文: You operate the elevator from here and I’ll go up.
    "Cinematic_330_01": "你在这儿操控电梯，我上去。",
    # 英文: I’ll go up.
    "Cinematic_330_02": "我上去。",
    # 英文: You’re the man.
    "Cinematic_330_03": "你真行。",

    # --- Cinematic 350 ---
    # 英文: Find him, take care of him.
    "Cinematic_350_01": "找到他，解决掉他。",

    # --- Cinematic 360 ---
    # 英文: NYPD! Freeze!
    "Cinematic_360_01": "纽约警局！别动！",
    # 英文: Easy! Don’t move!
    "Cinematic_360_02": "冷静！别动！",
    # 英文: Payne! What are you doing?
    "Cinematic_360_03": "佩恩！你在干什么？",
    # 英文: What are you doing?
    "Cinematic_360_04": "你在干什么？",
    # 英文: The million dollar question I didn’t have the answer to.
    "Cinematic_360_05": "这是个价值百万的问题，而我答不上来。",

    # --- Cinematic 380 ---
    # 英文: It was all connected,
    "Cinematic_380_01": "这一切都有关联，",
    # 英文: the murder of Senator Gate, the cleaners,
    "Cinematic_380_02": "盖特参议员的谋杀案，清洁工组织，",
    # 英文: the Inner Circle, Vinnie Gognitti.
    "Cinematic_380_03": "核心集团，还有维尼·戈尼提。",
    # 英文: I had to make Winterson see it.
    "Cinematic_380_04": "我得让温特森看清这一点。",
    # 英文: Winterson’s phone was ringing. She wasn’t at her desk.
    "Cinematic_380_05": "温特森的电话在响。她却不在座位上。",
    # 英文: Winterson’s phone.
    "Cinematic_380_06": "温特森的电话。",

    # --- Cinematic 390 ---
    # 英文: They are taking the fall, both of them.
    "Cinematic_390_01": "他们两个都在替人顶罪。",
    # 英文: Payne was with her when she was arrested.
    "Cinematic_390_02": "她被捕时佩恩和她在一起。",
    # 英文: Who are you talking to?
    "Cinematic_390_03": "你在跟谁说话？",
    # 英文: You are leaking information.
    "Cinematic_390_04": "你在泄露情报。",
    # 英文: Bravura’s too soft on you.
    "Cinematic_390_05": "布拉沃拉对你太手软了。",
    # 英文: I was informing the proper authorities on what they should know.
    "Cinematic_390_06": "我是在向有关当局通报他们该知道的情况。",
    # 英文: Stay away from my case, Max, stay away for your own good.
    "Cinematic_390_07": "离我的案子远点，马克思，为了你好就离远点。",
    # 英文: Everything had started out as black and white.
    "Cinematic_390_08": "一切开始时都黑白分明。",
    # 英文: Somewhere down the road the line went blurry.
    "Cinematic_390_09": "走到半途，那条界线却模糊了。",
    # 英文: The colors started to run, got smudged and gray.
    "Cinematic_390_10": "颜色开始晕开，变得污浊而灰暗。",
    # 英文: Winterson had been above my suspicion.
    "Cinematic_390_11": "温特森本不在我的怀疑之列。",
    # 英文: It felt like a goodbye.
    "Cinematic_390_12": "这感觉像一场告别。",

    # --- Cinematic 400 ---
    # 英文: Max!
    "Cinematic_400_01": "马克思！",
    # 英文: You’ve got to get me out of here.
    "Cinematic_400_02": "你得把我弄出去。",
    # 英文: You know I can’t do that.
    "Cinematic_400_03": "你知道我做不到。",
    # 英文: If I stay here, I’ll die.
    "Cinematic_400_04": "如果我留在这儿，我会死。",
    # 英文: Isn’t that a bit melodramatic?
    "Cinematic_400_05": "那是不是有点太戏剧化了？",
    # 英文: Behind bars, I’m a sitting duck.
    "Cinematic_400_06": "在牢里，我就是个活靶子。",
    # 英文: This is as safe as it gets.
    "Cinematic_400_07": "这儿已经是最安全的地方了。",
    # 英文: Come on, Max.
    "Cinematic_400_08": "拜托，马克思。",
    # 英文: Anyone of these cops could be on the Inner Circle’s payroll.
    "Cinematic_400_09": "这些警察里随便哪个，都可能收了核心集团的贿赂。",
    # 英文: You should know.
    "Cinematic_400_10": "你理应清楚。",
    # 英文: What’s that supposed to mean?
    "Cinematic_400_11": "你这话什么意思？",
    # 英文: You know Alfred Woden. You want answers, call him.
    "Cinematic_400_12": "你认识阿尔弗雷德·沃登。想要答案，就打给他。",
    # 英文: He'll verify everything I’ve told you.
    "Cinematic_400_13": "他会证实我告诉你的每一件事。",
    # 英文: Okay. I’ll do that.
    "Cinematic_400_14": "好吧。我会打的。",

    # --- Cinematic 410 ---
    # 英文: Jesus Christ!
    "Cinematic_410_01": "天哪！",
    # 英文: A bomb? That was a bomb!
    "Cinematic_410_02": "炸弹？那是个炸弹！",
    # 英文: Upstairs! Now!
    "Cinematic_410_03": "楼上！快！",
    # 英文: Jesus!
    "Cinematic_410_04": "天哪！",
    # 英文: Something was off.
    "Cinematic_410_05": "有点不对劲。",
    # 英文: Mona’s words on her being a sitting duck
    "Cinematic_410_06": "莫娜说自己是个活靶子的话",
    # 英文: kept playing in my head.
    "Cinematic_410_07": "一直在我脑海里回响。",
    # 英文: Upstairs, now!
    "Cinematic_410_08": "楼上，现在！",
    # 英文: The bomb had misdirection written all over it.
    "Cinematic_410_09": "这炸弹一看就是声东击西。",
    # 英文: Freeze! Drop it!
    "Cinematic_410_10": "别动！放下！",
    # 英文: Armed perps in the lockup! Officer down!
    "Cinematic_410_11": "羁押室有武装嫌犯！有警员倒下！",
    # 英文: Take him down!
    "Cinematic_410_12": "放倒他！",
    # 英文: Find the bitch! Find her, kill her!
    "Cinematic_410_13": "找出那个贱人！找到她，杀了她！",
    # 英文: NYPD! Drop your guns!
    "Cinematic_410_14": "纽约警局！把枪放下！",
    # 英文: Mona had been right. I had to go after her.
    "Cinematic_410_15": "莫娜是对的。我必须去追她。",

    # --- Cinematic 420 ---
    # 英文: Staying here, trapped behind a desk,
    "Cinematic_420_01": "留在这里，被囚在办公桌后，",
    # 英文: would have solved nothing.
    "Cinematic_420_02": "解决不了任何问题。",
    # 英文: Mona had vanished into the night.
    "Cinematic_420_03": "莫娜已消失在夜色中。",
    # 英文: Without her I had nothing to go on.
    "Cinematic_420_04": "没有她，我毫无头绪。",
    # 英文: I knew where to find her.
    "Cinematic_420_05": "但我知道去哪里找她。",

    # --- Cinematic 430 ---
    # 英文: This way!
    "Cinematic_430_01": "这边！",
    # 英文: Max!
    "Cinematic_430_02": "马克思！",
    # 英文: The trouble with wanting something is the fear of losing it,
    "Cinematic_430_03": "渴望某样东西的麻烦，在于害怕失去它，",
    # 英文: or never getting it.
    "Cinematic_430_04": "或者永远得不到它。",
    # 英文: The thought makes you weak.
    "Cinematic_430_05": "这种念头让你变得软弱。",

    # --- Cinematic 440 ---
    # 英文: There! She’s up there!
    "Cinematic_440_01": "那儿！她在上面！",
    # 英文: Look out!
    "Cinematic_440_02": "小心！",
    # 英文: The funhouse was Mona’s playground.
    "Cinematic_440_03": "那座游乐屋是莫娜的游乐场。",

    # --- Cinematic 460 ---
    # 英文: I was sick and tired of the cleaners speeding away in their vans.
    "Cinematic_460_01": "我受够了清洁工们开着面包车扬长而去。",
    # 英文: I had only one chance, no time to stop and think it through.
    "Cinematic_460_02": "我只有一次机会，没时间停下来思前想后。",

    # --- Cinematic 470 ---
    # 英文: Mona, Castling Insurance Companies construction site.
    "Cinematic_470_01": "莫娜，卡斯特林保险公司的建筑工地。",
    # 英文: I’m on my way.
    "Cinematic_470_02": "我这就过去。",
    # 英文: Take it to the top floor?
    "Cinematic_470_03": "把它带到顶层？",
    # 英文: Yeah, with the rest of the evidence.
    "Cinematic_470_04": "对，连同其余的证据一起。",
    # 英文: Hey, careful with those red boxes, you’ll blow us all up.
    "Cinematic_470_05": "嘿，那些红箱子小心点，会让我们全炸上天的。",
    # 英文: I’ll get the stuff from the van and meet you there.
    "Cinematic_470_06": "我去面包车里拿东西，在那儿跟你会合。",
    # 英文: Hey! What the f-
    "Cinematic_470_07": "嘿！你他妈——",

    # --- Cinematic 500 ---
    # 英文: This cleaner stuff’s made me think.
    "Cinematic_500_01": "这些清洁工的勾当让我起了疑。",
    # 英文: Didn’t use -
    "Cinematic_500_02": "没用上——",
    # 英文: Hey! There he is!
    "Cinematic_500_03": "嘿！他在那儿！",
    # 英文: We got him! We got him!
    "Cinematic_500_04": "我们抓住他了！我们抓住他了！",
    # 英文: No! Stop! The room’s full of explosives! Stop shooting!
    "Cinematic_500_05": "不！停下！这房间全是炸药！别开枪！",
    # 英文: Oh shit! Run! Run!
    "Cinematic_500_06": "哦该死！快跑！快跑！",
    # 英文: Max! What’s going on?
    "Cinematic_500_07": "马克思！怎么回事？",
    # 英文: The building’s blowing up, that’s what’s going on!
    "Cinematic_500_08": "大楼要炸了，这就是怎么回事！",

    # --- Cinematic 510 ---
    # 英文: Max? Max, what's happening?
    "Cinematic_510_01": "马克思？马克思，发生什么了？",
    # 英文: Max? Max, come in, can you hear me?
    "Cinematic_510_02": "马克思？马克思，收到吗，能听到我说话吗？",
    # 英文: Max? Max, answer me! Max!
    "Cinematic_510_03": "马克思？马克思，回我话！马克思！",

    # --- Cinematic 530 ---
    # 英文: Mona, I know this sounds crazy,
    "Cinematic_530_01": "莫娜，我知道这听起来很疯狂，",
    # 英文: but I need you to go and call the cops.
    "Cinematic_530_02": "但我需要你去报警。",
    # 英文: I need them here.
    "Cinematic_530_03": "我需要他们来这儿。",
    # 英文: You’re right, you are crazy.
    "Cinematic_530_04": "你说得对，你确实疯了。",
    # 英文: I’m a fugitive, Max. I just escaped from custody.
    "Cinematic_530_05": "我是个逃犯，马克思。我刚从羁押中逃出来。",
    # 英文: I wouldn’t ask if -
    "Cinematic_530_06": "若不是走投无路，我也不会开口——",
    # 英文: Go to hell, Max.
    "Cinematic_530_07": "下地狱去吧，马克思。",
    # 英文: Bastard.
    "Cinematic_530_08": "混蛋。",

    # --- Cinematic 540 ---
    # 英文: Throw the rules out of the window,
    "Cinematic_540_01": "把规矩扔出窗外，",
    # 英文: odds are you’ll go that way too.
    "Cinematic_540_02": "你多半也会那样坠落。",
    # 英文: Max? Max!
    "Cinematic_540_03": "马克思？马克思！",
    # 英文: This hadn’t been my first fall in the night.
    "Cinematic_540_04": "这已不是我夜里第一次坠落。",
    # 英文: Still just a prelude to the real deal,
    "Cinematic_540_05": "依然只是真正结局的前奏，",
    # 英文: still a long way to the bottom.
    "Cinematic_540_06": "离谷底还远着呢。",
    # 英文: There! Come on!
    "Cinematic_540_07": "那儿！快！",
    # 英文: Max! Company.
    "Cinematic_540_08": "马克思！来人了。",
    # 英文: Mona, you have to take them out, buy me time.
    "Cinematic_540_09": "莫娜，你得解决掉他们，替我争取时间。",
    # 英文: I couldn’t live without her.
    "Cinematic_540_10": "没有她，我活不下去。",

    # --- Cinematic 550 ---
    # 英文: Firing a gun is a binary choice.
    "Cinematic_550_01": "扣动扳机，非此即彼。",
    # 英文: You either pull the trigger or you don’t.
    "Cinematic_550_02": "你要么开枪，要么不开。",
    # 英文: Stop!
    "Cinematic_550_03": "停下！",
    # 英文: Stop. Wait.
    "Cinematic_550_04": "停下。等等。",

    # --- Cinematic 560 ---
    # 英文: Max.
    "Cinematic_560_01": "马克思。",
    # 英文: Oh Max.
    "Cinematic_560_02": "哦，马克思。",

    # --- Cinematic 610 ---
    # 英文: More cleaners! Waste them!
    "Cinematic_610_01": "更多清洁工！干掉他们！",
    # 英文: Get them before they get out!
    "Cinematic_610_02": "趁他们跑掉前截住他们！",

    # --- Cinematic 620 ---
    # 英文: Hey!
    "Cinematic_620_01": "嘿！",
    # 英文: Where the hell have you been? What took you so long?
    "Cinematic_620_02": "你他妈去哪了？怎么磨蹭这么久？",
    # 英文: Where’s the rest of you?
    "Cinematic_620_03": "你其他人呢？",
    # 英文: You’re the reinforcements Vinnie promised us, right?
    "Cinematic_620_04": "你就是维尼答应派给我们的援军，对吧？",
    # 英文: Who else? Only it’s just me, the cleaners got the rest.
    "Cinematic_620_05": "还能有谁？可惜只有我一个，其余的被清洁工解决了。",
    # 英文: Goddammit! They’re killing us like flies.
    "Cinematic_620_06": "该死！他们像拍苍蝇一样把我们干掉。",
    # 英文: I guess one extra gun is better than nothing.
    "Cinematic_620_07": "我想多一把枪总比没有强。",
    # 英文: Okay, let’s go.
    "Cinematic_620_08": "好，走吧。",

    # --- Cinematic 630 ---
    # 英文: Aw, man! Why did this have to happen to me?
    "Cinematic_630_01": "哎，老兄！这种事怎么偏偏落我头上？",
    # 英文: Aww. It was so perfect. Now it’s ruined.
    "Cinematic_630_02": "唉。原本那么完美。现在全毁了。",
    # 英文: Aw no! No way!
    "Cinematic_630_03": "啊不！没门！",

    # --- Cinematic 640 ---
    # 英文: They’re coming to kill me!
    "Cinematic_640_01": "他们要来杀我！",
    # 英文: You gotta protect me, we gotta get out of here.
    "Cinematic_640_02": "你得保护我，我们得离开这儿。",
    # 英文: Through the back yard!
    "Cinematic_640_03": "从后院走！",
    # 英文: I didn’t buy Vinnie’s promise to help me.
    "Cinematic_640_04": "我没信维尼会帮我的承诺。",
    # 英文: But I was willing to do anything to complicate Vlad’s plans.
    "Cinematic_640_05": "但我愿意不择手段，去搅乱弗拉德的计划。",
    # 英文: Payne! Cover me!
    "Cinematic_640_06": "佩恩！掩护我！",
    # 英文: Cover me! We gotta get through there.
    "Cinematic_640_07": "掩护我！我们得穿过那里。",

    # --- Cinematic 690 ---
    # 英文: Stay with it,
    "Cinematic_690_01": "盯紧它，",
    # 英文: and you can live a lifetime in that split second.
    "Cinematic_690_02": "你便能在那转瞬即逝的一刻里，过完一生。",
    # 英文: Besides,
    "Cinematic_690_03": "况且，",
    # 英文: a gentleman always avenges the insults done to his lady.
    "Cinematic_690_04": "绅士总会为加诸其女士的侮辱复仇。",
    # 英文: You did kill Winterson.
    "Cinematic_690_05": "你确实杀了温特森。",

    # --- Cinematic 700 ---
    # 英文: That won’t help a thing.
    "Cinematic_700_01": "那无济于事。",
    # 英文: The bullet in my head brought me to you.
    "Cinematic_700_02": "我脑中的那颗子弹，把我带到了你面前。",

    # --- Cinematic 710 ---
    # 英文: Showtime.
    "Cinematic_710_01": "好戏开场了。",
    # 英文: I’ll go down first. Cover me from here.
    "Cinematic_710_02": "我先下去。你在这儿掩护我。",
    # 英文: There! Alert! They’re here!
    "Cinematic_710_03": "那儿！警戒！他们来了！",
    # 英文: Damn!
    "Cinematic_710_04": "该死！",
    # 英文: Mona!
    "Cinematic_710_05": "莫娜！",

    # --- Cinematic 720 ---
    # 英文: I’ll climb down.
    "Cinematic_720_01": "我爬下去。",
    # 英文: No. Stay there.
    "Cinematic_720_02": "不。待在那儿。",
    # 英文: I’ll take the first floor, you take the second.
    "Cinematic_720_03": "我去一楼，你去二楼。",
    # 英文: Okay.
    "Cinematic_720_04": "好。",
    # 英文: I’m not sure I can -
    "Cinematic_720_05": "我不确定我能不能——",
    # 英文: Incoming!
    "Cinematic_720_06": "有来袭！",

    # --- Cinematic 740 ---
    # 英文: Dead end. Damn it.
    "Cinematic_740_01": "死路一条。该死。",
    # 英文: Here, let me.
    "Cinematic_740_02": "这儿，让我来。",
    # 英文: This way.
    "Cinematic_740_03": "这边走。",
    # 英文: Mona knew the manor. She was working for Woden.
    "Cinematic_740_04": "莫娜熟悉这座庄园。她在为沃登干活。",
    # 英文: Vlad had told me the truth.
    "Cinematic_740_05": "弗拉德告诉了我真相。",

    # --- Cinematic 750 ---
    # 英文: The killing has gone too far.
    "Cinematic_750_01": "杀戮已经太过分了。",
    # 英文: I have only begun.
    "Cinematic_750_02": "我才刚刚开始。",
    # 英文: It’s better to reign in hell than serve in heaven.
    "Cinematic_750_03": "宁在地狱称王，不在天堂为奴。",
    # 英文: I felt the rise of that old familiar feeling. I hated it.
    "Cinematic_750_04": "我感到那熟悉的老感觉又升起了。我痛恨它。",
    # 英文: You flatter yourself.
    "Cinematic_750_05": "你太抬举自己了。",
    # 英文: Demented fool!
    "Cinematic_750_06": "丧心病狂的蠢货！",
    # 英文: I welcomed it.
    "Cinematic_750_07": "我却欢迎它。",
    # 英文: Everything was clear again.
    "Cinematic_750_08": "一切又清晰起来。",
    # 英文: No more ambiguities, no more questions.
    "Cinematic_750_09": "不再有暧昧，不再有疑问。",
    # 英文: No gun when you need one.
    "Cinematic_750_10": "该用枪时偏偏没枪。",
    # 英文: One last thing left to do.
    "Cinematic_750_11": "还剩最后一件事要办。",
    # 英文: I was compelled to give Vlad his gun back.
    "Cinematic_750_12": "我不得不把枪还给弗拉德。",
    # 英文: One bullet at a time.
    "Cinematic_750_13": "一颗子弹，一次解决。",
}
