### 连续丧亲，再加上拿到了错误的诊断书，误以为自己身患胃癌的月宫夏音，在医院的天台准备自杀时，却被突然出现的小林悠介入。小林悠不仅没有劝阻，反而用毒舌的方式拆解死后的惨状，令夏音暂时退缩。临别时，悠自称是神明派来的天使，提议为夏音实现愿望。

label chapter_1_start:
    #1
    window hide
    scene black
    play sound "audio/sfx/sfx_001.mp3" loop fadein 1.0
    $ renpy.pause(0.5, hard=True)
    show screen intro_text_screen("听说，人从十米高的地方跳下去就会摔死。") with Dissolve(1.0)
    $ renpy.pause(2.0, hard=True)
    hide screen intro_text_screen with Dissolve(1.5)
    $ renpy.pause(1.0, hard=True)
    
    
    #2
    play music "audio/bgm/BGM_001.mp3"
    scene bg rooftop cloudy:
        subpixel True
        zoom 1.15 
        yalign 0.5 
        xalign 0.0         
        linear 30.0 xalign 1.0
    with Dissolve(1.0)
    window show
    with dissolve
    $ renpy.pause(1.0, hard=True)

    
    pov "市民医院的屋顶。{w=1.0}"
    pov "我站在天台边上，低头数着安装在墙壁上的白色空调机箱。"
    pov "一个，{w=1.0}两个，{w=1.0}三个..."
    pov "从上到下一共六台，距离地面大概二十多米。"
    pov "从这里跳下去，一定必死无疑吧。"
    pov "......"
    pov "四月快要结束了，气温稍微暖和了一点。"
    pov "不久前下过一场小雨，天空灰蒙蒙的，大块的积云盘踞在上空，像是套上了一层罩子。"
    pov "真是个和自杀再适合不过的天气了。"

    #3
    pov "我闭上眼睛。"
    scene bg_rooftop cloudy:
        blur 20
    with Dissolve(1.0)
    scene black with Dissolve(1.5)
    pov "指尖失去力气，诊断书随风飘落在地上。"
    pov "空气中混杂着泥土和青草的气息。"
    pov "深呼吸了一口，原本狂跳不止的心脏逐渐恢复平静。"

    #4
    stop sound
    scene bg living room:
        blur 15
    with Dissolve(2.0)
    window show 
    with dissolve
    $ renpy.pause(1.0, hard=True)

    p_nvl "迄今为止，我几乎没碰上过什么好事。"
    p_nvl "和大多数女孩子一样，我出生在普通的家庭，过着平淡的日子。"
    p_nvl "我曾经以为，这种理所当然的日常，会一直持续下去。"
    p_nvl "然而小学时，一场车祸却将父母的生命夺走了。"
    nvl clear

    #5
    scene bg countryside:
        subpixel True 
        zoom 1.15
        yalign 0.5 
        xalign 0.0
        linear 30.0 xalign 1.0
    with fade
    $ renpy.pause(1.0, hard=True)
    p_nvl "父母去世后，祖母将我接到老家，承担起抚养我的责任。"
    p_nvl "那时的我还很小，什么也不懂，只是每天魂不守舍地将自己关在狭小的房间里哭个不停，完全不愿意接受现实。"
    p_nvl "直到后来我才明白，在那段灰暗的日子，祖母为我付出了太多。"
    p_nvl "年过七十的祖母，不仅要照顾我的起居，还要每天想尽办法来安抚我。"
    p_nvl "意识到再这样逃避下去，只会增加祖母的负担，我才试着改变自己，重新回到了学校。"
    nvl clear

    p_nvl "话虽如此，在学校里，我也只是一个人阴沉地待在角落罢了。"
    p_nvl "我从来不开口说话，也不参加任何活动，甚至连体育课都不去。"
    p_nvl "老师和同学最初还会说些‘请加油’，‘不要放弃’之类的漂亮话，但时间一久，都对我避而远之了。"
    p_nvl "这是自然。"
    p_nvl "毕竟，谁会愿意把时间浪费在我这么一个麻烦的人身上呢？"
    p_nvl "我就像是一盆无法移走的腐烂植物，成天散发着令人不快的臭味。"
    nvl clear

    p_nvl "不过，我并不在乎。"
    p_nvl "我唯一的念头就是读完高中，再找份工作，让祖母不要再过那么辛苦的日子。"
    p_nvl "然而，就是这个小小的愿望，我也无法实现。"
    nvl clear
    $ renpy.pause(1.0, hard=True)
    p_nvl "一个月前，祖母也去世了。"
    nvl clear

    scene bg tap with fade
    $ renpy.pause(1.5, hard=True)
    p_nvl "祖母去世后，我自暴自弃地躺在家里，彻底成为了一个废人。"
    p_nvl "待在家里的我什么都不做，渴了就喝自来水，实在饿的不行，才会去超市买一些打折面包。"
    p_nvl "至于其他时间，我几乎都在睡觉。"
    p_nvl "只有睡着了，才能忘记那些令人难受的事情。"
    nvl clear

    p_nvl "这种动物般的生活持续了整整两周，我的身体状况也越来越差。"
    p_nvl "从最初的头晕恶心，到腹部疼得难以忍受。"
    p_nvl "最后迫不得已，才前往市民病院。"
    p_nvl "留院观察一天后，诊断书下来了。"
    nvl clear

    scene black with fade
    $ renpy.pause(0.5, hard=True)
    p_nvl "{size=80}{b}胃癌。{/b}{/size}"
    $ renpy.pause(0.5, hard=True)
    nvl clear
    p_nvl "白纸上的小字模糊不清，唯有那两个加粗的字符如同滚烫的烙印，填满了视线。"
    p_nvl "晃悠悠地离开房间，等回过神来时，已经到了天台边上。"
    nvl clear

    window hide
    scene bg rooftop cloudy with fade
    window show
    with Dissolve(1.0)
    $ renpy.pause(0.5, hard=True)
    pov "胃癌，我知道这是什么意思。"
    pov "就算去最好的医院，买最贵的药，也不过多苟延残喘几天。"
    pov "更何况，我的存款早就开始见底了。"
    pov "与其孤独地死在出租屋里，还不如现在就从这里跳下去。"
    pov "至少，还能够早点解脱。"
    pov "下定决心，我用力握紧了眼前的围栏。"
    pov "翻过去吧。"
    pov "只要翻过去，一切就都能够结束了......"


    #6
    window hide
    stop music
    camera:
        yoffset 20
        linear 0.03 yoffset -20
        linear 0.03 yoffset 20
        linear 0.03 yoffset -20
        linear 0.03 yoffset 15
        linear 0.03 yoffset -15
        linear 0.03 yoffset 10
        linear 0.03 yoffset -10
        linear 0.03 yoffset 5
        linear 0.03 yoffset -5
        linear 0.03 yoffset 0  
    $ renpy.pause(1.0, hard=True) 
    play sound "audio/sfx/sfx_001.mp3"
    unkown "喂，你在做什么呢？"
    pov "突如其来的声音将我吓了一跳。"   
    pov "转过头，只见身后不知何时站着一名少女。"
    play music "audio/bgm/BGM_002.mp3" 
    show you dress normal 1 with Dissolve(0.5)
    

    #7
    window show
    with dissolve
    $ renpy.pause(0.5, hard=True) 
    pov "......"
    pov "是同一间病房的人......"
    pov "虽然基本没在病房里待过，但因为长得很漂亮，让我对她有点印象。"
    pov "白皙的皮肤，小巧的脸庞，是那种在学校里绝对很受男孩子欢迎的类型。"
    pov "但是，我不是男孩子，突然闯入的陌生人，只会让我感到不快而已。"

    #8
    lin "站那里可是很危险的。"
    lin "还是说......你想要跳下去？"
    lin "啊，那是你的诊断书吗？我能看看吗？"
    show you at yuu_updown(0.3,935)
    $ renpy.pause(0.6, hard=True)
    pov "我还没来得及说话，她就自顾自地捡起被扔在地上的诊断书。"

    lin "喔喔，胃癌啊，年纪轻轻的还真是不走运。"
    lin "......"
    lin "你该不会......是因为这个才想自杀吧？"
    lin "......"
    lin "真的假的？"
    lin "再考虑一下比较好哦？父母可是会伤心的。"
    
    #9
    yin "父母早就......."
    pov "说到一半，我才意识到没有必要和她白费口舌，于是狠狠瞪了过去。"
    yin "话说和你没关系吧！你谁啊？"
    lin "啊哈哈，别露出那么可怕的表情嘛。"
    lin "而且，什么叫没关系，面前可是有一个活生生的人想要跳楼哦？"
    lin "再怎么说也没办法做到假装看不见吧。"
    yin "什么意思，难道你想阻止我吗？"
    
    #10
label test:
    stop music fadeout 1.0
    pov "胸口生出一股无名的怒火。"
    pov "身体因为愤怒而发抖，我忍不住攥紧了拳头。"

    play sound "audio/sfx/sfx_003.mp3"
    yin "你以为你是谁啊？{w=0.5}少在那儿装好人了，你懂我的什么？{w=1.0}" with vpunch
    yin "{size=+10}{b}{color=#ffffff}亲人全死光了是什么感受你知道吗？！{/color}{/size}{/b}" with hpunch
    yin "{size=+6}什么都不懂的家伙就别在那儿装模做样彰显同情心了！{/size}{w=0.5}" with hpunch