﻿

#注释：立绘名称
#al=艾琳
#ale=爱丽儿
#hfl=华芙琳

#init python:
    # 这个for循环的范围根据实际图片总数修改，这里假设总共5张图
    #for i in range(1, 6):
        #renpy.image("bg_image size_i" + str(i), "bg_size/bg" + str(i) + ".png")

# 游戏在此开始。

label ch1_1:




    show bg 31 with dissolve

    show bg with hpunch

    scene black with dissolve
    hide bg

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。



    scene bg 61:
        zoom 1.1
        xalign 0.5 yalign 1.0
        block:
            linear 0.35 xoffset 30
            linear 0.35 xoffset -30
            repeat

    play music "audio/bgm/ost11.mp3"

    "女孩" "哈……哈……"#（喘气声）

    """
    晌午时分，天空黑暗得仿佛太阳从未存在。

    尽管早已迷失了方向，但女孩仍在拼命奔跑，仿佛对她而言重要的只是奔跑，在哪里跑、跑去哪里并不重要。

    女孩不敢抬头。魔族的结界魔法覆盖了天空，背生双翼的魔族们在上空盘旋，密集地轨迹仿佛要把天空切成碎块。

    那些邪恶残暴的生物，正带着粘稠的恶意将她最珍视的东西夺去。

    令人安心的家与母亲所做的热汤，这都已遥不可及。

    孤身一人的女孩只能不断向着不知通往何处的森林深处奔跑，连周围的鸟叫声，都像嘲弄她一般。
    """

    show bg 61:
        xalign 0.0
        yalign 1.0
        linear 0.5 zoom 2.0 xalign 1.0


    "女孩" "呀……！"


    "女孩被树枝绊住脚步，身体重重摔在石子与树根盘结的地面。膝盖和手指上传来的疼痛令她的喘气都一瞬间停滞，连衣裙也破得不成样子。"
    scene bg 66:
        zoom 1.5 yalign 0.65 xalign 0.75
    show black:
        alpha 0.65
    with MoveRight

    """
    她已经精疲力尽，勉强翻过身才发现，这里正开着蓝白交错的细小野花。

    这个地方有些熟悉。

    这是曾经和父母一起聚餐，充满欢声笑语的地方。

    ——她又回到了原地。
    """
    play sound "audio/se/6.6.mp3"
    scene bg 61 with QMoveup:
        zoom 2.0
        xalign 0.5
        yalign 0.0

    narrator "狂风掠过树林上方，伴随着破碎的枝叶，身形巨大的人型生物巨锤般砸在不远处。在扬起的灰尘中，魔族猩红的双眼直盯着女孩。他缓缓起身，高达两米的身体上肌肉膨胀血管虬结，背后黑色的蝙蝠翅膀，正兴奋地扇动着。"
    scene bg 61 with dissolve

    """
    魔族狞笑着，故意一步一步地接近女孩，他的每一步都让地面轻微震颤，似乎想要继续这场追逐的游戏。

    即使女孩想要站起，颤抖的关节已经不受自己控制。眼泪、汗水和血液，一滴一滴渗透进土地之中。
    """

    "女孩" "爸爸妈妈……"
    """
    站立在树上的乌鸦放声大声着。

    这座巨大的肉山正在靠近。

    女孩指节发白，绝望地望着眼前的一切，泪水支离破碎地淌下。
    """
    "女孩" "救救我……"
    stop music

    #这里

    play sound "audio/se/8.mp3"
    show bg 10 as sword1:
        xpos 1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve

    pause 0.7

    play sound "audio/se/8.mp3"
    show bg 8 as sword2:
        xpos -1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve

    pause 0.7

    play sound "audio/se/8.mp3"
    show bg 22 as sword3:
        xpos 1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve

    pause 1.5

    scene bg 61
    with dissolve

    show bg 5 with light
    narrator "瞬息间，光影交错，银光闪动，魔族胸口传来一声炸响，魔族噔噔往后连退数步。"
    show bg 10 with QMoveLeft

    narrator "一柄银色短刃，不偏不倚地插在魔族胸膛。"
    show danger
    pause 0.5
    show bg 32 with dissolve
    narrator "魔族士兵目眦欲裂，正要发出声音，血液阻塞了他的喉咙。数秒后，肉山轰然倒塌，溅起一片血花。"


    #这里

    show bg 32 as blood1:
        xpos 2.0 ypos 1.0
        linear 0.1 xpos 0.0 ypos 0.0
    with dissolve
    pause 0.5
    show bg 28 as blood2
    with dissolve
    pause 1.0

    narrator "女孩睁开因害怕而紧闭的双眼。"

    scene bg 62
    with hpunch

    """
    一位与自己年龄相仿的少年于半空落下，从魔族胸口拔起那柄粘血的银色短刃。

    他身着贴身的黑色甲胄，体型瘦削干练，肌肉的线条俨然已经过锤炼。

    在确认了魔族已经丧命后，他转头看向女孩。随后，属于人类军队的密集脚步声从周围传来。
    """

    "少年" "你还好吗？"
    "女孩" "呜、呜……没事……"
    "女孩想要站起身来，但是无力的双腿直接让她再一次扑倒在地上。"
    "少年" "能站起来吗？需要我帮忙吗？"
    "少年拉着女孩的手将她从地上拉起，但是浑身脱力的女孩几乎完全只能靠在他身上。"
    "明明已经安全，女孩的眼泪却愈发控制不住。"
    "女孩" "呜、呜呜……"
    "面对泪流满面的女孩，少年表情局促手足无措，向周围张望一下后，下定了某种决心。"
    "他蹲下身体，从地上摘下一朵蓝色的小花，然后轻轻放在她手中。"
    "少年" "放心吧，已经安全了。"
    "少年" "我会保护你的。"

    # （接op，这里以后加cg,现在没有cg只能先只有背景了，不过也不一定，没有cg的话，会让玩家猜少女是谁，到时候再看看）
    pause

    scene bg prairie
    play music "audio/bgm/mo2.mp3"
    show hfl 1:
        xalign 0.5 yalign 0.0

    """
    空旷的草原上，一位穿着轻薄铠甲、身形矫健的少女正手持木剑不断朝我进攻。

    我的青梅竹马，华芙琳正在为明天的骑士团长选拔考试而努力。

    华芙琳的剑术和招式都是由我教导，我对于她每一瞬间的视线和重心的移动都了如指掌。
    """

    show bg 9 with dissolve:
        zoom 1.1
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        repeat 10

    "利用武器之间的撞击瞬间变换木剑的轨迹、以及利用衣摆遮挡下盘伪装重心的转移，这些小技巧她已经完全糅合进了自己华丽的剑姿中。"
    "但我专注防守，将她的剑一招一式尽数格挡开。"
    scene cg7 with light

    """
    少女蓝色的眸子中逐渐布满焦急之色，豆大的汗珠随着发梢飘散在剑风中。

    变得急促的呼吸和失去节奏的步伐，令她的剑技出现破绽。

    我瞅准木剑相交的刹那变换身形，瞬间闪身到她空门大开的左侧。

    “赢了！”
    """
    play sound "audio/se/5.mp3"
    show bg 27 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.0
        easein 0.25 xalign 0.5 yalign 0.5
    show bg with hpunch

    "被我一击肘击直冲护胸的华芙琳顿时失去平衡摔倒在草地上。"
    lloris "还好吗，华芙琳？"
    scene bg 27 with dissolve
    show hfl 4 :
        xalign 0.5 yalign 0.0
    with moveinbottom

    "少女起身擦了擦身上的土，皱着眉头再度向我举起剑。"
    warfarin "……洛里斯，你刚刚用了魔法是吧。"
    lloris "嗯？我有说过不能用魔法吗？"

    show hfl 5 with dissolve

    "华芙琳咬紧了嘴唇，随后眨眼间猛然放出一记极快的突刺！"
    warfarin "明明是剑术训练的！"

    show white:
        linear 0.05 alpha 1.0
        linear 0.05 alpha 0.0
        repeat 2
    pause 0.1
    scene bg 1 with hpunch

    "用剑侧打在她剑尖的轨迹，我一脚踢在她几乎悬空的下盘。"
    lloris "这招太急了。"
    "少女因此完全失去平衡，一连在草地上翻了几个跟头。"

    #这里
    scene black with MoveDown
    show bg 67:
        zoom 1.5 yalign 1.0

    show hfl 5 :
        xalign 0.5
        yalign -0.25
        zoom 1.2
    with MoveDown

    "不知道她是不是完全放弃了反抗的打算，她干脆大字平躺在草地上，目光空洞地望着天空。"
    lloris "刚刚就速度而言很棒哦，第一次把冲击魔法用在战斗上就能做到这个程度，已经很好了。"

    show hfl 2 with dissolve

    warfarin "……我还以为，刚才那下一定会赢的。"
    lloris "哈哈，再接再厉吧。"
    "即使是我这样说，她也没有像是以前那样爬起来再打一场。"
    lloris "怎么了？要休息了吗？"
    "华芙琳望着天空，喃喃自语。"
    warfarin "……要怎么样，才能像洛里斯那么强呢？"
    warfarin "都已经这么久了，一次都没有赢过……"
    "我把剑放在一边，在她身边坐下。"
    lloris "这个嘛，倒不如说华芙琳为什么这么想要变强？"
    "她伸出手，将木剑举在自己眼前。"
    warfarin "因为我想加入骑士团，就像是父亲和哥哥那样。"
    warfarin "大家都觉得女孩子不适合当骑士，但是我才不想当温室花朵……"
    lloris "嗯嗯，然后呢？"
    warfarin "我也不想输给哥哥……"
    warfarin "还有，要上战场杀敌，把那些可恨的魔族全部驱逐干净……"
    lloris "哦……"
    "华芙琳好像注意到了我短暂的沉默，马上翻身坐直身体。"

    show hfl 8:
        linear 0.35 xalign 0.5 yalign 0.0

    warfarin "啊，我不是说爱丽儿妹妹和莉莉丝阿姨不好的意思！我是说……那些烧杀抢掠的坏魔族们……"
    lloris "放心，我知道的。"
    warfarin "总、总之，我的意思就是说……要是世界可以和平、不用继续战争就好了……"
    lloris "我觉得很好啊。"

    show hfl 3 with dissolve

    warfarin "那，洛里斯为什么这么强呢？"
    lloris "嗯……"
    "我看向坐在身边的蓝发少女，身后的夕阳正在缓缓沉入深褐色的田野。"
    lloris "因为我受过严格的训练。就是这样。"
    "华芙琳瞪大双眼，而后气恼地捶在我的肩膀上。"

    show hfl 4  with dissolve

    warfarin "什么嘛！我还期待从你口中说出什么远大的理想！"
    lloris "我可没有那种东西。"
    lloris "再说，有谁规定过信念和实力有必然联系吗？"
    warfarin "就、就算是这样……历代的骑士团长都是又有实力又有信念的……"
    warfarin "比如我父亲那样……"
    lloris "或许是吧，但在我看来，兼具实力和人格魅力的人设，如今差不多变成单纯的宣传口号了。"
    "华芙琳刚想反驳什么，但最终却慢慢偃旗息鼓。"
    "自从五年前的战争以来，原本保护地方安全的骑士团已经完全变得唯实力论。素质考核名存实亡，就连骑士团长的职位也可以由不是骑士的人参与选拔。而且，利用骑士身份欺男霸女的事件，也屡见不鲜。"
    warfarin "虽然是这样啦……"
    lloris "所以说，这个世界需要那些既有信念又有力量的人来指引道路才行。"
    "我看向华芙琳，轻轻抚摸她的脑袋。"
    lloris "我一直觉得，华芙琳未来就会成为这样的人。"

    show hfl 8 :
        ease 0.09 xoffset 10
        ease 0.09 xoffset -10
        repeat 2

    "华芙琳呆愣地看了我一会儿后，脸颊绯红地瞥向一边。"
    warfarin "……没想到洛里斯对我评价这么高。"
    lloris "嗯？我没说过我很喜欢华芙琳的剑技吗？"

    show hfl 6  with dissolve

    warfarin "这种话你一次都没说过啊。"
    "华芙琳抱着膝盖，缩着肩膀小声说道。"
    warfarin "我还以为，洛里斯你肯定觉得帮我训练剑术很无聊呢……"
    lloris "怎么会。我可是一直期待着华芙琳成为骑士团长的。"

    scene bg 24
    with dissolve

    "就在我们如此闲谈之中，夕阳快要完全沉入到地平线下，时间已经不早。"
    lloris "那么，我们回去吧。"

    show hfl 6  with dissolve:
        xalign 0.5 yalign 0.0

    warfarin "嗯。"
    "虽然这么说，华芙琳站起身时却疼得龇牙咧嘴。"
    warfarin "刚才……用冲击魔法时崴到脚了……"
    "第一次将魔法用在剑术战斗，控制不了力度是常有的事。这种伤势用治愈魔法很快就能治好，可惜这类魔法对于我们两人都不是强项。"
    lloris "没办法，我背你回家吧，我会拜托爱丽儿帮忙的。"

    show hfl 7  with dissolve

    warfarin "谢谢你……"
    "将华芙琳背在背上，我向着家的方向出发。"
    "不知道是不是因为害羞，华芙琳只是紧紧抱着我的肩膀，一言不发。"

    scene bg 14
    with fade

    play music "audio/bgm/mo1.mp3"

    "赤红的太阳收敛了它的光辉，在夕阳上方浅白的云层上，深蓝的星星正逐渐从夜空中浮现。"
    warfarin "我想起，小时候的事情了。"
    "趴在我身上的少女，用自言自语般的音量小声说着。"
    lloris "什么？"
    warfarin "在洛里斯去战场的之前的事情了……还记得吗？"
    warfarin "那是我们总是在外面疯玩一整天，下午玩累了你就背着我回家……"
    "华芙琳坐直身体，看向遥远的夕阳。"
    warfarin "就好像一切都没变一样……"
    "我将华芙琳掂了掂。"
    lloris "……"
    lloris "……可能吧。"
    warfarin "你这家伙，刚才是不是想说什么？"
    warfarin "想说的话，可以直接说出来哦。"
    lloris "哪有哪有。"
    show black with dissolve
    "…………{p}……"

    scene bg 52

    show ale 5 as ale:
        xalign 0.5 yalign 0.0
    with fade
    ariel "呀~哥哥回来了！"
    """
    刚刚走进家门，一位体型娇小的金发女孩就坏笑着迎了上来。

    我同父异母的妹妹，爱丽儿，绕着圈子打量着紧贴在一起的我们两人。

    本来想在她发现之前把华芙琳放下来的，结果被她撞了个正着。
    """

    show ale 9 as ale:
        easein 0.35 xalign -7.0 yalign 0.0
    show hfl 1 with dissolve:
        xalign 1.5 alpha 0.0
        easein 0.35 xalign 1.0 yalign 0.0 alpha 1.0

    ariel "咦？哥哥背上背着的是什么？是哥哥的战利品？"
    warfarin "爱、爱丽儿……"
    "华芙琳求饶似的声音从背后传来。"
    ariel "啊哈哈，仔细一看，这不是华芙琳姐姐吗！"
    ariel "怎么今天比起往常还要腻歪呢？"
    warfarin "只、只是崴到脚拜托洛里斯背我一下而已啦！"
    ariel "对了对了，对于这种娇弱的战利品，应该用公主抱才更合适哦，哥哥！"
    lloris "这个话题你还真是不厌烦……"
    ariel "但是哥哥也不讨厌，对吧？"
    lloris "不讨厌什么的……"
    ariel "难道说其实是喜欢？"

    show ale 4 with dissolve
    show hfl 8 :
        ease 0.1 yoffset -20
        ease 0.1 yoffset 0


    warfarin "这、这个……！"
    lilith "爱丽儿，别太让华芙琳为难。"
    """
    拥有一头靓丽金发的妇人从房间中走出来，那便是我的继母莉莉丝，爱丽儿的亲生母亲。

    她有着魔族的血统，那辉光闪烁的红色眼眸就是其特征。

    我的亲生母亲因为难产而死，而真正担负起养育责任的就是莉莉丝阿姨本人。

    从这个意义上来说，与其说是继母，不如说更接近于母亲。
    """

    show hfl 1  with dissolve

    warfarin "莉莉丝阿姨。"
    "华芙琳礼貌地向她问好，而她也微笑着回应。"
    "我将华芙琳放在椅子上。"
    lloris "爱丽儿，拜托用治愈魔法帮华芙琳恢复一下伤口。今天练剑的时候不小心让她受伤了。"
    ariel "我说哥哥，你还没回答我的问题呢。"
    "爱丽儿又一个劲儿地凑上前来，笑着问我。"
    ariel "哥哥是喜欢华芙琳姐姐的吧？"
    lloris "什么喜欢不喜欢的……"

    # 画面：cg0 画面闪烁
    #这里
    scene white
    show cg0:
        alpha 0.2
        zoom 0.9
        block:
            linear 1.0 alpha 0.3
            linear 1.0 alpha 0.2
            repeat
    with dissolve
    "在某一瞬间，我的眼前闪过了某位儿时玩伴的身影。那个总是忧郁地望着天空的黑发女孩。"
    "也不知道她现在过得怎么样……"
    lloris "我们只是朋友而已。"

    scene bg 52 with dissolve

    play music "audio/bgm/ost14.mp3"

    eberl "朋友？"
    show fq 1:
        zoom 0.75 alpha 0.0 xalign 1.5
        easein 0.45 alpha 1.0 xalign 0.5

    "威严的声音从房门处响起，一个高大的身影推门走了进来。"
    "他身着黑底金边的圣教袍，头发花白，散发着来自于上位者肃穆稳重的气质。"
    "这名男人是我的父亲，教会圣父之一，埃布尔。"
    "和华芙琳用简单的点头打过招呼后，他看向我这边。"
    eberl "练剑练得这么开心，到底有没有进步？"
    "莉莉丝阿姨似害怕又似敬畏，小心翼翼地帮他取下装饰华丽的圣教袍。"
    lilith "大人，欢迎回家，最近政事怎么样了呢。"
    "父亲并未理会莉莉丝阿姨，目光严厉地等我做出回答。"
    lloris "我正在努力，父亲。"
    "我只得低下头，如此回答。"
    "他似乎并不满意我的回复，径直走到我面前，自上而下地盯着我。"
    eberl "我看你每天倒是玩得开心。你还记得你自己的责任吗？"
    lloris "……是。"
    eberl "抬起头看着我！你的声音怎么像个小姑娘一样？马上把你刚才的话重新说一遍！"
    "我迅速挺起胸膛。"
    lloris "是，我保证不会辜负您的期望！"
    eberl "哼，不要忘记自己军人的身份！就算是和平时期，也要时刻警戒，不得懈怠，记住了吗？"
    "随后，父亲将目光移到旁边的莉莉丝阿姨身上。"
    eberl "莉莉丝，你跟我走。"
    "他不再多说什么，转身走出了家门，莉莉丝阿姨只得亦步亦趋地跟上，留下我们愣在原地。"

    show ale 9 at left:
        xalign -13.0 yalign 0.0
    show hfl 6 at right:
        xalign 1.43 yalign 0.0
    with dissolve
    play music "audio/bgm/ost4.mp3"

    "自从刚才起一直藏在我身后的爱丽儿，像是受惊的小鸟般揪着我的衣角。"
    "父亲他向来就是如此喜怒无常。除了超出常识的严厉外，在对于我的训练上有着近乎偏执的执念。"
    "不如说，除了训练我之外，他几乎没有别的爱好。"
    "得益于他从小就进行的严格训练，我拥有了还算是出色的剑技。而也在他的刻意安排下，我从小就进入了骑士军累积战功，至今有了相当的军衔。"
    "但他对莉莉丝阿姨和爱丽儿仿佛不抱有任何的兴趣。她们两人因为魔族的血统备受白眼，而他有着显赫的地位，却连解释的努力都不愿意付出，甚至在家时也几乎不向爱丽儿搭话。"
    "我轻轻抚摸爱丽儿的头发。"
    lloris "乖……"
    "爱丽儿将我的衣角抓得更紧。"
    warfarin "那个……抱歉。"
    "华芙琳担心地说到。"
    lloris "不，我才应该抱歉。"

    scene black
    with fade
    #这里先黑屏，等2个月左右后插cg88

    "在爱丽儿释放完治愈魔法后，华芙琳以要准备明天的选拔考试为由先行离开了。"
    "之后在只有两个人的家里，我和爱丽儿一起吃了晚饭。夜色渐深，爱丽儿就像是往常那般撒着娇要和我一起睡。"
    "爱丽儿早就已经有了自己的房间，我理应拒绝，但她却还是坚持要和我一起睡。"
    "但想到爱丽儿躲在我身后时的表情，我只好同意了她。"
    "…………"
    "……"

    #1-2

    scene bg prairie with slow_light
    play music "audio/bgm/ost6.mp3"

    "清晨的第一缕阳光从窗户的缝隙照进房间，替还在熟睡的爱丽儿压好被子后，我带上木剑来到了昨天的草地。"
    "下午就是华芙琳参与骑士团长选拔的时间，这就是她的最后一次训练了。"

    show hfl 1 with dissolve:
        xalign 0.5 yalign 0.0

    "紫发的少女已然整备完毕，穿着骑士铠的她将长发扎成干练的马尾，笔挺的身躯仿佛已经是一位身经百战的骑士。"
    "望见我之后，她远远地向我挥手。"
    warfarin "洛里斯，这里这里！"
    lloris "久等了。看上去你已经完全准备好了。"

    show hfl 7 with dissolve

    "华芙琳挠着脸颊，露出了不好意思的笑。"
    warfarin "嗯，虽然昨天晚上紧张得没睡着就是了。"
    lloris "哈哈是吗。那么就尽力而为吧。"

    show hfl 1 with dissolve

    "在端正地将剑身彼此碰撞行礼之后，华芙琳深吸了一口气，从剑身传来的颤抖，也随着漫长的呼气变得平稳。"
    "某种凝练而稳定的气息，仿佛有生命般盘旋在她的四周。"
    "她闭上眼睛，少女姣好的面容上，浮现出无比专注认真的神情。"

    show hfl 1 with dissolve:
        alpha 0.0


    "……在第一次与她见面的时候，我是否预料到过会有这样的一天呢？"
    "小时候的她简直顽皮得像个男孩，真正意识到她其实是女孩子时，已经是我战争结束返乡的时候了。"
    "过去因为没有弄清楚她的性别而搞出的种种，时至今日，也依然令人莞尔一笑。"

    show hfl 1 with dissolve:
        xalign 0.5 yalign 0.0 alpha 1.0

    warfarin "我说，洛里斯。"
    lloris "怎么了？"
    "华芙琳睁开眼睛，蓝色的眼眸中没有任何杂质，我明白接下来要说的已经在她那里酝酿多时。"
    warfarin "要是我成为了骑士团长的话，可以实现我一个愿望吗？"
    lloris "如果我可以做到的话。"

    show hfl 7 with dissolve

    "她展露出笑容。"
    warfarin "谢谢你，洛里斯。"
    warfarin "要是没有你的话，一定就不会有现在的我。"
    warfarin "……具体的愿望，就在我拿下胜利后，请认真听我说吧。"
    lloris "嗯。"
    "我从不怀疑华芙琳会成为骑士团长，在军队呆过多年的我见识过各种各样的剑士，她的天赋在我所知的所有人之中也能达到前三之列。"
    "但这并不是最重要的东西。"
    "华芙琳的剑技与我不同。在战场练出的剑技只是目的单纯的杀人技，一切下作的、卑鄙的手段，只要是为了杀人，无所不用。"
    "而华芙琳的剑技华丽而矫健，每招每式都带着坚韧的精神，毫不动摇。"
    "无论是谁，只要见到了华芙琳的剑技，都会明白她是一个怎样努力的少女。"

    play music "audio/bgm/ost13.mp3"
    scene bg 18 with ccirclewipe

    """
    在与她进行完最后的剑术对练后，我送她来到骑士团的练武场上。

    砖石结构的圆环形建筑中，参赛手们从另一边的入口进入。而我则跟随前来看热闹的人群，来到观众席。

    练武场内的戒备森严，扎在城楼顶端的长枪冷光闪烁。在中央圆形场地上一侧的裁判席高台上，一位大约四五十岁的身穿重铠的中年人，正坐在席位中间。

    那正是华芙琳的父亲，现任的骑士团长，曾经在前线战场上声名显赫，但是在某次战斗负伤之后，身手已经大不如前。

    过去好几次去华芙琳家和他见过面。虽然平时看上去是个性格温和的大叔，但对华芋琳几乎已经到达了溺爱的程度，不仅从来不许她接触武器，就连华芙琳受了一点擦伤都要唠叨半天。也正是因为如此，华芙琳才会拜托我帮她训练剑技。

    初赛的选拔模式为一对一的淘汰制战斗，使用的武器和铠甲都是骑士团提供的制式装备。

    大多数抱着侥幸心理的参赛者早已在预选上淘汰，经过为数不多的几场战斗后，华芙琳终于来到了决赛的擂台。

    为了更真实地模拟战场的环境，最后的决战为五人混战。

    在这种情况下几乎无所谓胜利的条件，即使打倒一个人，其他参赛者也并不会因此停下手中的武器。

    也就是说，只有将所有敌人打出擂台或者是令对方主动投降才能获得真正的胜利。

    在这种赛制上，受伤在所难免。

    我在的位置看不清骑士团长的表情。但想来，他多半不会预料到自己的女儿已经能够站上这样的舞台了。

    战鼓阵阵响起，旗帜在风中猎猎作响。
    """

    #插Cg11,3，从左往右，先放大后恢复正常。  做的时候素材缺失
    #这里

    "华芙琳穿着和训练时一般无二的轻甲，手持未开锋的单手铁剑。"
    "仅仅是站在原地，她的身影就散发出鲜明的存在感，令同样站在擂台上的其余四人黯然失色。"
    lloris "不妙啊……"
    "华芙琳太过专注了。"
    "华芙琳的一举一动都吸引着观众们的注意，仿佛她本身具有着某种牵动人心的力量。"
    "她毫不掩饰自己的气势，这样多半就会在一开始遭到其余四人的围攻。"
    "若是我，我大约会伪装成在先前的战斗中负伤不轻以避免成为集中攻击的目标，等到参赛者减员后再坐收渔利。"
    "但正因如此，我坚信华芙琳才是真正适合成为骑士团长的人。"

    #画面闪烁
    #这里

    scene black with dissolve


    "裁判" "选手各就各位……开始！"
    show bg 8 with hpunch:
        alpha 0.0
        easein 0.35 alpha 1.0
    play sound "audio/se/18.mp3"
    show bg 10 with hpunch:
        alpha 0.0
        easein 0.35 alpha 1.0
    play sound "audio/se/19.mp3"
    show white with light
    "随着裁判一声令下，金铁交鸣声响成一片。"

    # 画面：cg7
    # 从左往右，先放大后恢复正常
    scene cg7 with dissolve:
        zoom 1.8
        xalign 0.0 yalign 0.5
        linear 2.0 xalign 1.0
    pause 2.3
    scene cg7:
        zoom 0.9
        xalign 0.5 yalign 0.5
    with dissolve
    play sound "audio/se/19.mp3" loop
    """
    正如我所预料，华芙琳成为了其他参赛者的第一攻击目标。长枪、短刃、巨剑、重锤顿时向她周身袭来。

    但她架势丝毫不乱，猛然间伴随一声轻喝，其中一位参赛者武器便已经脱手而出。

    面对围攻时首先集中攻击一个人正是正确的做法。

    华芙琳在其余几人的剑势中辗转腾挪，竟不过数十秒就脱离包围圈。她剑尖一转，身作弓步，转守为攻。

    另外几人面面相觑，眼看围攻战术失败，只好各自拉开距离互相提防。

    华芙琳从来不会等待别人主动进攻。在他人拉开距离还未站定的瞬间，一声炸响从她脚下传来，瞬息之间她已经逼近其中一人，伴随一道乌黑的剑光，对方的武器应声而飞。
    """
    show white:
        linear 0.05 alpha 0.0
        linear 0.05 alpha 1.0
        linear 0.05 alpha 0.0
        repeat 2
    play sound "audio/se/10.mp3"
    """
    这等华丽而迅捷的一击顿时赢得了场上阵阵欢呼。

    在短暂调息后，她再次将突刺的起手式对准另外一人。"""
    show bg 22:
        zoom 1.5 xalign 1.0 yalign 1.0 alpha 0.0
        easein 0.45  xalign 0.0 alpha 1.0
    pause 0.5
    play sound "audio/se/10.mp3"
    scene white with light
    """她已经完全将冲击魔法融入了自己突刺的剑技之中。五人混战，仅数回合华芙琳就战胜了两人。

    剩下的两人，一人是胡子拉碴的雇佣兵，另一人则是猎手模样。以两人先前的战斗来看，他们都不是此时的华芙琳的对手。"""
    scene black with dissolve
    show bg 8 with slash
    play sound "se/18.mp3"
    pause 0.45
    show bg 10 with slash_2
    play sound "se/19.mp3"
    pause 0.15
    show cg7 with light
    """猎手深知不应该再给予华芙琳使出突刺的机会，迅速迂回着试探进攻，但即便如此，几回合之后猎人手中的武器便被华芙琳疾风骤雨般的快攻打落。

    他们错失了围攻华芙琳的最后机会。可以说，华芙琳胜局已定。
    """
    "选手A" "我不服！凭什么一个女孩可以当上骑士团长！她就算现在能赢过我们，这种小毛孩根本领导不了骑士团！"
    "雇佣兵头上青筋暴起，大声咆哮，但看台上只响起了一片嘘声。"

    scene bg 24
    show hfl 4 :
        xalign 0.5 yalign 0.0
    with dissolve
    warfarin "用实力来证明吧。"
    """
    华芙琳在连续几次突刺中消耗了大量体力，但是架势丝毫不乱。

    雇佣兵怒吼着挥舞起双手重剑，虽然体型庞大却步伐灵活，能站到这个擂台绝非浪得虚名。

    他似乎已经看出华芙琳已经没有足够体力马上使用刚才的高速突刺，狞笑着将那重剑向华芙琳拍来。那巨大的惯性绝非华芙琳可以用单手剑格挡，若不能以速度和灵活取胜，只能被他一步一步逼到场地边缘。

    但若是华芙琳在那之前就恢复了体力再次使用那一记突刺，以巨剑的笨重难以防御。

    华芙琳一路躲闪，寻找时机,眼看着她已经被退到擂台边缘。

    突然之间，雇佣兵浑身肌肉膨胀，速度陡然提升一倍有余，带着一往无前的气势使出一记力量速度兼具的横扫千军！

    此时此刻即使是华芙琳使出突刺也无法冲破这一招的架势，身体娇柔的少女面对势大力沉的巨剑已经避无可避！

    任何人都明白接下来就是决定性的时刻。
    """
    hide hfl

    "但眨眼间，华芙琳从所有人的视线中消失了。"
    "随后，雇佣兵就像是被弹飞了般摔下擂台，只留下汗水岑岑的紫发少女蹲在原地。"

    play sound "audio/se/14.mp3"
    show bg 79
    with slash
    show white:
        linear 0.05 alpha 0.0
        linear 0.05 alpha 1.0
        linear 0.05 alpha 0.0
        repeat 2
    narrator "在刚才那一转瞬，华芙琳用一记上挑击偏了巨剑横扫的轨迹，随后迅速压低身形踹在了他的小腿上，令他被巨剑的惯性扔出了场外。"
    narrator "……这正是我昨天曾对她使用过的招式。"
    scene bg 24 with light
    narrator "周围的人群爆发出震耳欲聋的欢呼，就连裁判席上的骑士团长都忍不住起身鼓掌。"


    show hfl 1 :
        xalign 0.5 yalign 0.0
    with moveinbottom

    "少女擦了擦额头上的汗珠，兴奋地站起身，好像在寻找谁般扫视着观众席。"
    "比赛已经结束，剩下的就只是些繁琐的仪式和场面话。想必华芙琳会成为最近很长一段时间里小镇上的新闻吧。不久之后，她也会正式地接任骑士团长的职务，实现自己的梦想已经近在眼前。"
    "于是我站起身，离开演武场。"
    "今天晚上，她家里大概会通宵地庆祝，在此之前准备好礼物才合适。"

    #1-3

    stop music fadeout 3.0

    scene bg 73
    with fade

    play sound "audio/se/9.mp3"

    """
    已经是黄昏时分，入夜的寒意也随之降临。

    我漫步在小镇上，因为骑士团长选拔的缘故，街道人流稀少。

    从北方吹来的冷风，预示着寒冷的冬季即将到来。
    """
    play music "audio/bgm/ost17.mp3"

    lloris "……"
    "有什么不对劲的地方。"
    "街道上，实在是太过安静了。"
    show black with MoveRight
    scene bg 74
    with MoveRight
    play sound "audio/se/6.6.mp3"

    """
    视野尽头的森林，在夕阳的另一端，已经被黑夜吞没。家畜哀嚎的声音在空无一人的街道中隐约回响。

    某种不祥的预感从脊背攀附而上，我放弃买礼物的打算，转而开始向家的方向快步前进。

    爱丽儿和莉莉丝阿姨因为魔族的血统，不方便去到演武场那种人群聚集的地方。

    在数分钟后我才发现，小镇上方的天空中，某种异常熟悉的黑暗正在快速扩散。
    """
    scene bg 23
    with fade

    "这是魔族的结界魔法！"
    lloris "糟了！"

    scene bg 74 with QMovedown
    show bg with hpunch

    """
    我猫腰藏进路边的灌木丛，一股一股隐晦的黑色波动正在街道上蔓延。

    天空中的黑暗飞速汇聚，数次呼吸间夕阳已经完全消失不见。

    魔族军队最擅长打闪电战，独有的结界魔法覆盖整片区域更是他们通常的做法。利用结界精准定位强者后发动远距离魔法斩首，剩余的平民则通常会被困在结界之中玩弄致死。

    但这里不是前线，魔族的爪牙怎么会延伸到这种地方。更何况发动如此大规模的魔法，难道他们又想发动一场全面战争吗！
    """
    "？？" "救命……救命啊……！"

    "一个女人瘸着腿在街道上走着，她披头散发衣服破败。街道上少有的几个行人被吸引了注意力，向她那边走去。"

    # 画面：bg 28，32
    # 强调闪烁
    # 我不知道血液的闪烁效果应该做成什么样的，所以从沿用了上面的代码
    #这里

    show bg 32 as blood1:
        xpos 2.0 ypos 1.0
        linear 0.1 xpos 0.0 ypos 0.0
    with dissolve
    pause 0.5
    show bg 28 as blood2
    with dissolve

    """
    但就在他们接近女人的一瞬间，行人如碎纸般被撕碎成块，游荡的妇女伴随着躯干的爆炸四肢飞散，残尸遍野，鲜血淋漓，断壁残垣之上，破碎内脏伴着碎骨髓液撒了一地，死状凄厉，惨不忍睹。

    血腥味扑鼻而来，空气因此变得格外粘稠。

    这是魔族惯用的人肉陷阱。

    他们在俘虏身上埋下炸弹再放回到一般城镇中，一旦这种炸弹周围的人数到达规定值就会发生剧烈爆炸。
    """

    lloris "混账……！"

    play sound "audio/se/2.mp3"

    #后来新增了画面s01晃动的说明

    """
    地面传来隆隆的响声，数分后一波背生双翼双目通红的异化魔族士兵碾过街道。

    我没带武器，此时战斗绝非明智之举。

    等到魔族大军暂时离开，我潜入城镇小巷，沿着近路急速向家的位置狂奔。

    爱丽儿和莉莉丝不知道会怎样，必须马上回去才行！

    一路上不断见到粉碎成红色肉泥的尸体，对于现状的预估不断降低，内心的不安如同挥之不去的阴影令人心情沉重。

    …………

    ……
    """

    scene bg 52
    with fade

    "回到家时，不过是五六分钟后。因为持续不断的狂奔，喉咙和胸口正不断抽痛。"
    lloris "爱丽儿！莉莉丝阿姨！"

    show ale 6 as ale:
        xalign 0.5 yalign 0.0
    with dissolve
    play music "audio/bgm/ost12.mp3"

    lilith "洛里斯！"
    ariel "哥哥！"
    "家中一切照旧，没有魔族入侵的痕迹。"
    "莉莉丝阿姨担心地快步冲过来，抓住我的手。爱丽儿也跑过来紧紧抱住我。"
    "家也在魔族结界的笼罩范围之内，两人看上去都因为这种仿佛吞没天地的黑暗而紧张不已。"
    lilith "还好你没事！"
    lloris "嗯！时间紧张，你们快藏到地下室去！"
    ariel "哥哥，镇上发生什么事了？"
    lloris "……魔族发动了进攻。"
    lloris "现在不是说这个的时候，爱丽儿，快去！"
    ariel "哥哥你呢？"
    "爱丽儿丝毫不撒手，娇小的身体因为恐惧而不断颤抖着。"
    lloris "我还有别的事情。"

    show ale 7 as ale
    with dissolve
    ariel "哥哥你是不是要上前线了！我不要你走，留下来跟我和妈妈一起！"
    lilith "爱丽儿，别任性！"
    "莉莉丝阿姨大声呵斥爱丽儿。"
    ariel "不要！不要！"
    lloris "爱丽儿，放心。"
    "我轻轻抱住爱丽儿，拍着她的不断颤抖的身体。"
    lloris "这是我的责任。"

    show ale 8 as ale
    with dissolve
    ariel "但是、但是……！"
    lloris "我绝对会保护你们。"
    "爱丽儿泪眼婆娑地看着我，而后再次将我紧抱住。"

    show ale 6 as ale
    with dissolve
    ariel "……那约好了。"
    lloris "嗯。"
    ariel "哥哥一定要平安回来。"
    lloris "放心吧。"

    scene bg 21
    with dissolve
    with dissolve
    "将两人带进地下室，我回到自己的房间穿上甲胄，取出放在剑架上的银色短刃。"

    show bg 31
    with fade
    with dissolve
    "这是在遥远的孩童时代父亲送给我的生日礼物。即使在这和平的五年中不再使用，在父亲的督促下我并没有停下对它的日常保养。"
    "一切就绪。"

    #1-4

    scene bg 29
    with fade
    play music "audio/bgm/ost13.mp3"

    """
    魔族最擅长闪击战，这黑暗的封闭结界已经是他们进攻的标志。

    这种魔法范围巨大且极难击破，甚至兼具侦测、远距离打击、封闭等功能，但也有个巨大的缺陷——这魔法极其显眼。

    即使是数十公里外，也能够清晰地看到这突兀的黑色巨蛋。

    但粗略估计，其他镇上发现这边的异样到调集兵力支援，至少也需要两三个小时。

    因此可以推测，发动这场奇袭的指挥官，认为可以在三个小时之内达成目的。

    ……但是说到底，魔族为什么会发动这场战争？

    街道上已经一片狼藉，属于人类的断肢和内脏散发着恶臭，猩红的液体在街道横流。

    黑夜已经降临，天空中的黑暗变得更加深邃。

    我径直通过最短路径朝着练武场狂奔。

    如果我没猜错，这个镇上的战斗人员因为骑士团长的选拔考试几乎都集中在练武场。因此练武场也必定是魔族士兵们的集中攻击目标。

    距离魔族发动入侵已经接近一个小时。
    """
    lloris "必须再快一点……！"
    lloris "华芙琳，一定要平安无事！"
    scene black with MoveRight
    stop music fadeout 3.0
    "…………"
    "……"

    scene bg 53
    with MoveRight
    play music "audio/bgm/ost10.mp3"

    """
    演武场。

    黑色的硝烟弥漫。城楼上的长枪已经被轰炸得七零八落。

    无论何处，都散布着大量砖块和人类的尸体。

    第一波远程魔法轰炸落在了观众席。原本密集的人群就像是被一只大脚碾过，只留下一地长达数十米的肉酱。魔法爆炸的硫磺味以及内脏的腥臭，令人作呕。
    """

    "骑士A" "咳……咳咳……"
    "骑士B" "这下该怎么办……"

    """
    仅剩的数名骑士正持剑站在擂台中央，但他们的体力显然已经不支。

    周围不断涌出背生双翼的异化魔族，他们瞪着猩红的双眼，以嘲弄的目光盯着众人。

    这些残暴的魔族们以折磨为乐，他们故意留下这几人，只是为了欣赏人类挣扎的模样。

    悬殊的人数比不存在任何胜利的可能。骑士们显然知道这一点，强作镇定的表情掩饰不住他们的恐惧，他们战战兢兢，连手中的剑一不留神就会脱手。
    """

    show hfl 6 :
        xalign 0.5 yalign 0.0

    with dissolve
    "华芙琳正站在众人的前列，身体正因愤怒不断颤抖。"
    "她的父亲被第一波远程的魔法轰炸波及，随后被迅速出现的魔族士兵俘虏。此时那位中年人已经失去意识，被魔族用绳索吊在只剩下残垣断壁的裁判席上。"
    "将敌人的指挥官当做俘虏示众，是他们玩乐的手段，也是最快瓦解敌人斗志的办法。"

    "魔族指挥官" "嘻嘻，你们已经没有胜算，差不多扔下武器了吧？"

    "为首的魔族不像其他魔族那般肌肉膨胀，而是身着长衫，一头金发闪闪发光，带着金边圆框眼镜，鲜艳的红色嘴唇仿佛渗着血。"
    "从他华丽的服饰来看，任谁也能看出他就是发动这次奇袭的指挥官。"

    show hfl 4
    with dissolve
    show bg with hpunch
    warfarin "不要动摇！坚持到援军到来！"
    "华芙琳向其他骑士大喝一声，打断了魔族指挥官的话。"
    "魔族指挥官露出不悦的表情，用小指指着华芙琳，舔了舔嘴唇。"
    "魔族指挥官" "没人教过你，不要随便插话吗？小妹妹？"

    show hfl 5
    with dissolve
    #原文是   华芙琳（愤怒）：“……”

    warfarin "……"
    "随即，魔族指挥官就像是想到什么一般露出邪恶的笑容。"
    "魔族指挥官" "哦？在来之前我看过你的资料……"
    "魔族指挥官" "那边吊着的那位，是令父吧？"
    "华芙琳愤怒得眼睛快要喷出火来。她瞪视着魔族指挥官，一言不发。"
    "魔族指挥官" "嘻嘻嘻，看来的确如此。正好这里是你们人族的练武场……不如我们来玩个游戏？"
    "他随手从地上捡起一根木棍，当做是武器般随手挥舞两下。"
    "魔族指挥官" "按照你们人族的说法，叫做……剑术对练？"
    "魔族指挥官" "当然，我可以绅士地照顾你，只使用这根木棍，而你……可以使用你手上那把铁剑。"
    "魔族指挥官" "只要你伤到我一丁点，我就可以放掉你和在那边发抖的几个人……"
    "他随即残忍地舔着嘴唇。"
    "魔族指挥官" "但是作为代价，要是你被我打中一次，我就会砍掉令父的一肢体……"
    "愤怒的火焰从华芙琳的脚下直冲头顶，她双目通红，手中的铁剑被她握得嘎吱作响。"

    show hfl 4
    with dissolve
    warfarin "……我要杀了你。"
    "华芙琳咬牙切齿。"
    "魔族指挥官" "那就是，同意咯？"
    "魔族指挥官掩嘴大笑，漆黑的双翼从他背后展开。形成实质的气流从他周身猛然喷发，无数灰尘在场地中飞扬。"
    "魔族指挥官" "小妹妹，别眨眼。"
    "魔族指挥官" "游戏，开始咯。"
    "瞬息间，魔族消失不见。"
    "这并非障眼法，而是因为极致的速度超越了人眼所能捕捉的极限。"
    scene cg7:
        zoom 0.9
        xalign 0.5 yalign 0.5
    with dissolve
    "华芙琳瞳孔紧缩，以野兽般的直觉将剑挡在身后。"
    "伴随着一声巨响，华芙琳被击飞出去，但她立刻受身重新架起剑势。"
    "站在她先前所在位置的魔族指挥官，饶有兴致地看着自己手中的一段紫色长发。"
    "魔族指挥官" "头发，也算是命中了哟。"

    scene cg2:
        zoom 0.45
        xalign 0.5 yalign 0.5
    with dissolve


    "华芙琳转头看向自己父亲所在的方向，一个魔族士兵拿起砍刀，手起刀落地从大臂斩断了她父亲的右手。"
    "血液从断面喷涌而出，断肢在绳子上晃荡，只剩下肩部的右臂无力地垂下。"
    "魔族指挥官" "哎呀，这下子就没办法握剑了。"
    "魔族指挥官以嘲弄地口吻笑道。"
    warfarin "混账……混账……！"
    "华芙琳目眦欲裂，身如闪电地向魔族发起突刺。"
    "魔族指挥官" "没人教过你不要在这么远的距离突刺吗？"
    "他再度扇动翅膀消失不见。"
    "背生双翼的魔族天然就比人类多了一个移动器官，与人类战斗的经验很难直接套用在魔族身上。"
    "这一次他正正好好出现在华芙琳的上方，怪笑着高速甩动手中的木棍。"
    "魔族指挥官" "一次！"
    "迅捷的攻击抽在华芙琳的脸颊，血液从她的嘴里喷溅而出。"
    "华芙琳咬牙发出上挑，但这次魔族已出现在她身后。"
    "魔族指挥官" "两次！"
    "木棍如同鞭子般狠狠打在她的后背！"
    "华芙琳转变剑锋发出横斩却再次落空！"
    "魔族指挥官" "三次！"
    "魔族的声音从正上方传来，伴随着最后势大力沉的劈腿，华芙琳被重重砸进场地里。"
    "口腔中布满腥味，右边的脸颊肿了起来，右眼也完全睁不开了。"
    "魔族指挥官" "怎么？站起来啊！"
    warfarin "咳……咳咳……"
    "华芙琳强撑膝盖，用剑支起身体。"
    "身上的轻甲近乎完全破碎，鲜血从嘴角溢出。"
    "魔族指挥官" "你看看，都是因为你，你的父亲现在变成人棍咯？"
    "魔族指挥官" "还有一次咯？小姑娘，再不努力的话，你的父亲就要人头落地了哟？"
    "魔族指挥官" "不过现在也没好到哪里去就是了？还是说比起这种状态，死了才更好？"
    "一言不发的华芙琳，面无表情地再度举起剑。这样的事态让魔族感到相当地无趣。"
    "魔族指挥官" "……没意思，真没意思。我本来以为你是剩下人里面的最强者，没想到连这点乐趣都不能给我。"
    "魔族指挥官" "吝啬！实在是太吝啬了！"

    scene cg7:
        zoom 0.9
        xalign 0.5 yalign 0.5

    "华芙琳沉默地，身作弓步，再度摆出了突刺的起手式。"
    "魔族嘲弄地笑着，仿佛在看一只蚂蚁。"
    "魔族指挥官" "好吧。既然你坚持要用这招，那我就让你打中一下吧。"
    "魔族指挥官" "但是，你可千万要瞄准了，要是没有马上杀死我……"
    "魔族残忍地抿嘴。"
    "魔族指挥官" "后果，你可以想象吧？"
    "华芙琳安静地站着。刚才的那记劈腿已经让她内脏出血，即使闭上眼睛，雪花般的噪点依然在视网膜中闪烁。"

    #画面闪烁
    #这里
    show white:
        linear 0.05 alpha 1.0
        linear 0.05 alpha 0.0
        repeat 3
    pause 0.4
    show cg7 with light:
        blur 15

    """
    强烈的晕眩感干扰着她的感官，她几乎不能站直身体。

    周围的一切声音仿佛都在离她远去，万籁俱寂之中，连心跳和呼吸声都消失不见。

    在做了一次深呼吸后，她沉下重心，脚下展开冲击魔法，发出了最后的突刺。

    极快的速度将她身影拉成一条细线。
    """

    scene bg 5 with light

    "魔族指挥官" "长不了记性是吗！"
    "就在突刺过程中，一连串的爆鸣声从她的脚下响起，少女的身体再度加速。"
    "接着，在魔族的视野中，突然失去了华芙琳的踪迹。"
    "魔族指挥官" "怎么可能！"
    show bg 22 with dissolve:
        zoom 1.5 xalign 1.0 yalign 0.0
        easein 0.45 xalign 0.0 yalign 1.0
    "魔族面色骇然正欲后退，乌黑的剑尖已然抵在他的胸口！"
    "魔族指挥官" "不可能！人类怎么可能……！"

    play sound "audio/se/19.mp3"
    #效果音1

    "金属碰撞的声音响彻全场！"
    "魔族指挥官" "哈……哈……"
    """
    折断的剑尖掉落在不远处的地面。

    在魔族胸口破碎的长衫下，露出了里面的黑色护甲。

    少女手中的剑断成两截，她目光空洞，身体疲软地倒在地上。

    刚才她将全部的魔力转化为冲击魔法灌注在双腿上，如今她小腿往下部分的骨骼，已经变成无数破碎的骨片。
    """

    "魔族指挥官" "哈、哈哈、原来如此……呵呵哈哈哈……！"
    "确信自己胜利的魔族指挥官终于放声狂笑。"
    "魔族指挥官" "有意思！有意思！竟然做到这种程度！"
    "魔族指挥官" "如果不是你的武器太烂，刚才我就差点失手了！"
    "魔族指挥官" "没想到就连这种小镇，也有这种趣事！"
    "他捋开散在额头上的发丝，冷漠地盯着趴在地上的华芙琳，缓缓抬起脚。"
    "魔族指挥官" "现在，和你的脑袋说再见吧。"


    stop music fadeout 3.0

    #这里

    show bg 10 as sword1:
        xpos 1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve
    play sound "audio/se/19.mp3"

    pause 0.5

    show bg 8 as sword2:
        xpos -1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve
    play sound "audio/se/19.mp3"

    pause 0.5

    show bg 22 as sword3:
        xpos 1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve
    play sound "audio/se/19.mp3"

    pause 1.5

    #画面：10，8,22 音乐停止
    scene bg 32 with dissolve
    "血液飞溅。"
    "魔族指挥官" "呃……啊啊啊！"
    scene black with dissolve
    "…………"
    "……"

    play music "audio/bgm/ost13.mp3"
    scene bg 53
    with fade

    "我甩掉剑刃上魔族的血液。"
    "那斯文败类模样的魔族指挥官正跪在地面一个劲儿地哀嚎。"
    "魔族指挥官" "人族！畜生！……我的翅膀啊啊啊啊啊！"
    """
    如我所料，魔族的主要兵力集中在演武场这里。

    演武场已经被围得水泄不通，强硬突破绝非明智之举，我只能选择从高处用魔法径直坠落到演武场内部。

    事态不容乐观。剩下的数名骑士绝不是魔族军队的对手。而原本身为小镇最强者的骑士团长，已经被砍断手脚，失血过多濒死。

    而我身后的华芙琳也完全失去了意识。

    没有援军、伤者众多、甚至位于敌人包围圈内。

    可以说是最糟糕的事态。

    以理性而言，我不应该如此张扬地直接出现在这魔族指挥官面前，瞅准机会单独救走华芙琳的做法才是成功率最高的办法。

    毕竟以我个人的力量，无论如何也无法和一整支军队正面抗衡。
    """
    "魔族指挥官" "你！竟敢偷袭！你破坏了游戏！"
    "魔族指挥官歇斯底里地冲我大叫，但他右边的翅膀已经不能向以前那样扇动。"
    lloris "哈，游戏？你说的？"
    "魔族指挥官" "贱人！"
    "他拔出腰上的武器向我砍来，但失去了一边翅膀的魔族就像是瘸了一只脚的人类般破绽百出。"
    "我反手将剑刃插进他那只手关节中，无论何种铠甲，关节处总是弱点所在。"
    "魔族指挥官" "啊啊啊啊啊啊啊啊！"
    "他的武器掉在地上，抱着右手大声哀嚎。"
    lloris "怎么叫得像只丧家犬，刚才不是还很得意吗？"
    "魔族指挥官" "杀了、给我杀了他们！"
    lloris "是吗，那我劝你谨慎发言。"
    "手起刀落斩断魔族另一只翅膀后，我将剑搭在他的脖子上。"
    lloris "你看，这把剑可是很锋利的。"
    "魔族倒吸一口凉气。"
    "魔族指挥官" "混球、畜生……我要杀了你……！"
    lloris "别以为生气的只有你。你对我朋友做的这些事，我能忍住，我的剑不一定。"
    "魔族指挥官" "嘶……嘶……"
    "局势一时间陷入了僵持。"
    "周围魔族虎视眈眈地盯着我，等待着指挥官下达命令。之前已经精疲力竭的骑士们站到我身后，扶起华芙琳，检查她的伤势。"
    "骑士A" "洛里斯！她伤得很重！"
    "魔族指挥官" "哈……哈哈！"
    "魔族喘着粗气，勉强咧嘴笑着。"
    lloris "娘娘腔，你还有什么要说的。"
    "魔族指挥官" "嘻、嘻……那个人族女孩，我刚才特意下了狠手，再过十几分钟，她就会因为内脏出血死掉……"
    lloris "……"
    "魔族指挥官" "我们这么僵持，一点好处都没有……不如我们各退一步，我放过你们，你放过我……"
    lloris "哈哈，真冷静啊。不过我凭什么相信你？"
    "魔族指挥官" "……我可以先让你们出去。"
    "魔族指挥官向那些士兵打着手势，人群整齐地让开一条道路。不多时，骑士团长也被两个魔族搬过来，放在地面。"
    "他已经失去四肢，整个人看上去缩小了一圈。"
    "压下胸腔中跳动的漆黑愤怒，我示意骑士们抬起华芙琳和骑士团长，一步一退地押着魔族指挥官来到演武场外。"
    "魔族指挥官" "像你这样的强者，要不要来我们魔族？"
    "魔族指挥官突然说道。"
    "我忍不住笑出声来。"
    lloris "你应该在魔族的地位挺高的吧。"
    "魔族指挥官" "哼，没错，只要我开口，你想要什么官职都行……"
    "我将剑死死抵住他的颈动脉令他闭嘴。"
    lloris "我说，你的那些士兵靠的有点近了吧？"
    "他慌忙打着手势让士兵离远点。"
    "魔族指挥官" "差、差不多可以放开我了吧！"
    lloris "……"
    "我没有丝毫放开剑的打算。"
    lloris "……你觉得，我没有看出你的小动作？"
    "魔族指挥官" "什什么？"
    lloris "你的士兵，在骑士团长的身上安了人肉炸弹。你觉得我看不出来？"
    "魔族指挥官" "别动手……！"

    # 画面：10，8,22
    # 画面闪烁，闪烁怎么做
    #这里

    show bg 10 as sword1:
        xpos 1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve

    pause 0.5

    show bg 8 as sword2:
        xpos -1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve

    pause 0.5

    show bg 22 as sword3:
        xpos 1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve

    scene bg 32 with dissolve

    "手起刀落，他的人头已然落地。"
    "这个指挥官打着等我们远离后就马上引爆炸弹的算盘。那么在事情发生之前就杀了他才是正确做法。"
    "趁着魔族军队愣神的功夫，我径直向他们发起突刺。"
    play sound "se/18.mp3"

    scene bg 6 with slash
    show bg with hpunch
    # 画面震动

    lloris "你们带着华芙琳快走！我来拖住他们！"

    "混战再度打响！"
    play sound "se/18.mp3"

    scene bg 8 with slash
    # 画面震动
    show bg 10 as sword1:
        xpos 1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve
    play sound "se/18.mp3"

    pause 0.5

    show bg 8 as sword2:
        xpos -1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve
    play sound "se/18.mp3"

    pause 0.5

    show bg 22 as sword3:
        xpos 1.0 ypos -1.0
        linear 0.15 xpos 0.0 ypos 0.0
    with dissolve
    play sound "se/18.mp3"

    scene bg 32 with dissolve
    """
    数道剑光闪过，前面的魔族接连倒下。

    被突然杀乱阵脚的魔族一阵混乱，我以尽可能地以破坏他们的行动能力为目的开始战斗。

    在以一敌多的巷战环境中，不能行动的魔族成了绝佳的绊脚石。

    据袭击两个小时已经过去，援军还没到来，上一次面对如此数量的敌人，已经是五六年前。

    遥远的战斗记忆逐渐苏醒，我拼尽全力在魔族中冲撞。

    绕到背后砍掉他们的翅膀。

    把他们的身体当做抵挡魔法的肉盾。

    避开魔族锋利的爪牙，压低身体斩断他们的脚跟。

    肉体的疲惫在累积、精神的亢奋达到极致！

    还不够，还不够，还不够……！

    要在援军到来前保护住华芙琳，这点程度还远远不够！！！！
    """

    lloris "咳咳咳……！"

    scene bg 28
    with dissolve
    stop music fadeout 2.0

    #画面震动 音乐停止

    """
    不知道从什么时候开始，我的嘴角正渗出血。

    这是毒。

    不知道是那位指挥官下的毒，还是说这些士兵们带着的毒药，又或者是谁在隐蔽的角落用了什么魔法。

    心脏的声音震耳欲聋，全身的每一寸肌肉都在抽动。

    冷静、冷静下来。

    放弃一切的思考，将所有的注意力集中在战斗之中。

    麻木感从脊背攀附而上，视野被血液染红，意识开始离肉体远去。
    """

    # 画面：bg32，3
    # 画面震动，散开
    # 不会做
    #这里
    scene bg 32
    show bg 3
    with fade
    show danger
    show red:
        alpha 0.0
        linear 10.0 alpha 1.0

    """
    空白一片的脑海中，突兀地出现了一点猩红色。

    从未有过的膨胀的嗜血欲望，正在意识中飞速扩散。

    我仍在战斗。

    手中武器的存在变得无比鲜明。

    不断地、不断地，用被血脂磨钝的短剑，夺取敌人的生命。

    魔族的血液让那片猩红扩张着。

    直至将全部视野覆盖。

    …………

    ……
    """

    scene bg 15
    with fade

    play music "audio/bgm/ost7.mp3"

    """
    回过神来，我正站在开满蓝白小花的森林之中。

    我的手中没有武器，身上也只是普通的布衣。

    刚才剧烈到极致的战斗，就好像只是一场梦。

    心灵平静得不可思议，我仿佛回到了我本来应该在的地方。
    """
    show al 21 with dissolve:
        zoom 1.3
        xalign 0.5 yalign 0.0

    "少女" "……洛里斯。"
    "有人呼唤着我的名字。"
    "我转过身去，一位头上带着花环的黑发少女，正笑意吟吟地注视我。"
    lloris "……艾琳。"
    eileen "洛里斯，为什么在这里。"
    lloris "我不知道……只是，觉得好累。"

    show al 22 with dissolve

    "少女笑着，向我张开双手。"
    eileen "洛里斯，来这边。"
    show bg:
        linear 0.5 zoom 1.4
    show al:
        linear 0.5 zoom 1.7
    "我顺应着来到她的身边，然后，她踮起脚，将我的头抱在她怀里。"
    "从她身上传来了宛如花香的气息，伴随着她的体温，温柔得仿佛要将我融化。"

    show al 13
    with dissolve
    eileen "安心吧……洛里斯。"
    eileen "现在……还不是时候……"
    eileen "再努力一下下就好……"
    eileen "这一次，换我来保护你……"
    scene black with MoveDown
    "…………"
    "……"

    scene bg 25
    with fade
    show mrk1 as mrk:
        xalign 0.5 yalign 0.0
    with dissolve
    play music "audio/bgm/ost2.mp3"

    """
    身体沉重得仿佛不是自己的。

    鼻尖传来了百合花的香气。

    睁开眼睛，房间里的一切映入眼帘。

    干净整洁的床铺，摆在床头柜上的鲜花，以及趴在床边，沉沉睡着的爱丽儿。

    坐在另一边，翘着二郎腿的黄发青年正看着手中的书。

    ……那是我的好友，麦瑞克。

    不知为何，明明作为圣父A随从的他竟然在这里。

    注意到我视线的麦瑞克，看了看正沉沉睡着的爱丽儿，悄步走到我身边。
    """

    show mrk6 as mrk
    with dissolve
    "麦瑞克" "先别急着动，你的伤势不轻。"
    lloris "咳咳，华芙琳呢？"
    "麦瑞克" "你是说你的青梅竹马？"

    show mrk4 as mrk
    with dissolve

    "麦瑞克露出令人安心的笑容。"
    "麦瑞克" "放心吧，她好着呢。"
    "听上去我坚持到了援军的到来。"
    "我费力地支起身体，检查了一遍身体状况。"
    "至少在我昏迷的这段时间，没有少掉手脚或者脸上的器官。"
    "……又或许是，曾经少掉过，但是用高级的治愈魔法再生了。"
    lloris "麦瑞克，你在这里，难道说圣父们集合了？"
    "麦瑞克" "差不多。"
    "麦瑞克不置可否地笑了笑。"

    show mrk2 as mrk
    with dissolve
    "麦瑞克" "毕竟这次的袭击事关重大，圣父们这次是亲自带兵来救援。"

    "我翻身下床，披上旁边的外套，径直走出房间。"
    "外面嘈杂的人声扑面而来，四处穿梭的护士和治愈术士们，以及看不到头的白色帐篷，说明着情况的惨烈。"

    show mrk5 as mrk
    with dissolve
    "麦瑞克" "喂喂，你一直昏睡了三天了，别刚起床就乱动啊。"
    lloris "不行，得马上和圣父们商量对策！"
    "麦瑞克" "唉……真是急性子。"
    "麦瑞克叹了口气。"

    show mrk1 as mrk
    with dissolve
    "麦瑞克" "洛里斯，你跟我来，圣父们正好在开会。"
    "…………"
    "……"

    scene bg 64
    with fade
    play music "audio/bgm/ost16.mp3"

    "会议室正在举行着圣父们的会议。圣父们聚集一堂时只可能讨论决定国家命运的重要政事。"
    "但比起神圣，猜忌更适合形容这个场所。"
    "我拨开帐幕走进会议室，身着圣教袍的圣父们正整齐地坐在圆形议事桌前。"
    lloris "洛里斯参上，叩见各位圣父们。"
    show fq 1:
        xalign 0.5 yalign 0.0
    with dissolve
    "在身着华丽圣教袍的大人物中，父亲也在其中。"
    eberl "洛里斯，你到我后面来，现在我们正在商量对策。"
    "圣父甲" "魔族生来天性残忍，喜好杀戮，又会令人捉摸不透的暗魔法。我们的简单法术的圣骑士和中等法术的魔法师，难以抵抗他们。"
    "圣父乙" "拿近的来说，五年前的那次战争最后也只能通过割让土地换取暂且的和平。我们与魔族之间的实力，实在是悬殊太大了。"
    "圣父丙" "如今魔族大军已深入南边边界线领地，前线战事也是节节败退……"
    "圣父丙" "若是再拿不出对策，只会让我们损失更加惨重。这次的突然袭击也是如此，我们根本没有手段去预测魔族的结界魔法。"
    "父亲安静地听着其余圣父的谈话，似乎在等待发言的时机。"
    eberl "诸位，有关于军力一事，我有一法。"
    eberl "我正在研发一种能极快增强士兵体质的符贴，暂名赎罪券。有了这东西，即便是普通民众也能武力强大，肉体足以匹敌魔族。"
    "圣父甲" "埃布尔你此话可当真？"
    eberl "若是诸位想要亲眼观看，我会安排时间。"
    "父亲语出惊人，世上真有这种好东西？"
    "要是有这种东西，那为什么之前不拿出来？"
    eberl "赎罪券已经经过了充分的验证。若是诸位没有异议，相信本周内就能派上用场。"
    lloris "那这种赎罪券的原理是什么，是否对人类有副作用呢？"
    show fq 5 with dissolve

    "父亲严厉地瞪了我一眼，示意我不要随意插嘴。"
    show fq 1 with dissolve

    eberl "另外还有一事。此次洛里斯在城镇保卫战中立下了汗马功劳，我希望从即日起让他负责包含A区在内的骑士军统辖。"
    "圣父丙" "埃布尔，你莫不是在打什么算盘？"
    "圣父甲" "丙兄，洛里斯少年英雄，这次的功绩有目共睹。再加上附近正是他的家乡，让他负责这块再合适不过。"
    "圣父丙" "哼。行吧。但关于赎罪券的事，我们议会内部会好好考虑的。洛里斯将军你先退下吧！"
    "当前的气氛，已经不容得我插嘴，实在没有办法，我低下头，小声对父亲耳语。"
    lloris "父亲，您待会儿有空吗？我有事想问您。"
    show fq 5 with dissolve

    eberl "之后再说。"

    scene bg 36
    with fade
    show mrk5 as mrk:
        xalign 0.5 yalign 0.0
    with dissolve
    play music "audio/bgm/ost2.mp3"

    "几乎是被赶出营帐，我叹了口气，在外面等候的麦瑞克带着一副“我就知道”的表情看着我。"
    "麦瑞克" "洛里斯，别太着急了。"
    "麦瑞克拍拍我的肩膀。"
    "麦瑞克" "战斗还有的是，你再休息几天吧，以后可就要忙到死了。"
    lloris "谢谢。"
    "我摇了摇头，看向铺满视野的白色帐篷。"
    lloris "对了，骑士团长呢？"
    "麦瑞克" "在那边呢。"
    "我看向麦瑞克所指的方向。"

    scene bg 13
    with dissolve
    show hfl 3 :
        xalign 0.5 yalign 0.0
    with dissolve
    play music "audio/bgm/mo2.mp3"

    "在大量被临时放在地上的伤员之中，一位身穿骑士轻甲的紫发少女，正跟着旁边的护士替伤员们包扎伤口。"
    "额头上还扎着绷带的她，表情认真，专注的气质令人瞩目。"
    lloris "不是，我是说……"

    show hfl 6 with dissolve

    "少女似乎注意到我的视线，向我这边望来。在短暂地愣神后，露出了泫然欲泣的神情。"
    "她站起身，一瘸一拐地，慢慢向我走来。"
    "麦瑞克" "站着干嘛。"
    "麦瑞克猛一拍我的后背。"
    "华芙琳的膝盖上带着外骨骼支具，在先前的战斗中，因为过度使用冲击魔法而导致了粉碎性骨折。"
    warfarin "洛里斯……洛里斯！"

    show cg9 with dissolve
    # with fade

    "她噙着眼泪，在距离我数步之遥时，喜极而泣地扑进我怀中。"
    "一边的麦瑞克心领神会地笑了笑，走开了。"

    hide cg9 with dissolve
    # with fade

    show hfl 6 with dissolve

    lloris "华芙琳……"
    warfarin "你还好吗？洛里斯！"
    warfarin "我还以为，以后再也见不到你了。"
    lloris "放心，我没事……"
    lloris "对不起，当时我来晚了。"
    show hfl 3 with dissolve
    warfarin "不，谢谢你。"
    warfarin "大家，都因为洛里斯而得救了。"
    warfarin "父亲活了下来……洛里斯也还活着，真是……太好了。"
    scene cg9
    with dissolve
    "少女将脸埋在我的胸口，泪水打湿了我的衣服。我抱住她颤抖的肩膀，轻轻安抚她。"
    lloris "是啊……"
    "周围的伤员们微笑着看着我们，但没有一人起哄。"
    "就像是想要更多感受体温一般，华芙琳拦腰抱住我，紧紧地贴在我身上。"
    "突然之间，背后好像又有谁抱了上来。"




    return
