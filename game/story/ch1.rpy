### 连续丧亲，再加上拿到了错误的诊断书，误以为自己身患胃癌的月宫夏音，在医院的天台准备自杀时，却被突然出现的小林悠介入。小林悠不仅没有劝阻，反而用毒舌的方式拆解死后的惨状，令夏音暂时退缩。临别时，悠自称是神明派来的天使，提议为夏音实现愿望。

label chapter_1_start:
    #1
    window hide
    scene black
    play sound "audio/sfx/sfx_001.mp3" loop fadein 1.0 volume 0.5
    pause 1.0 
    show screen intro_text_screen("听说，人从十米高的地方跳下去就会摔死。") with Dissolve(1.0)
    pause 2.0 
    hide screen intro_text_screen with Dissolve(1.5)
    pause 2.0 
    
    
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
    pause 1.0 

    
    pov "市民医院的屋顶。{w=1.0}"
    pov "我站在天台边上，低头数着安装在墙壁上的白色空调机箱。"
    pov "一个，{w=0.7}两个，{w=0.7}三个..."
    pov "从上到下一共六台，距离地面大概二十多米。"
    pov "从这里跳下去，一定必死无疑吧。"
    pov "......"
    pov "四月快要结束了，气温稍微暖和了一点。"
    pov "不久前下过一场小雨，天空灰蒙蒙的，大块的积云盘踞在上空，像是套上了一层罩子。"
    pov "真是个和自杀再适合不过的天气了。"

    #3
    pov "我闭上眼睛。"
    scene black with Dissolve(2.0)
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
    pause 1.0 

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
    pause 1.0 
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
    pause 1.0 
    p_nvl "一个月前，祖母也去世了。"
    nvl clear

    scene bg tap with fade
    pause 1.5
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
    pause 0.5
    p_nvl "{size=80}{b}胃癌。{/b}{/size}"
    pause 0.5
    nvl clear
    p_nvl "白纸上的小字模糊不清，唯有那两个加粗的字符如同滚烫的烙印，填满了视线。"
    p_nvl "我晃悠悠地离开房间，等回过神来时，已经到了天台边上。"
    nvl clear

    window hide
    scene bg rooftop cloudy with fade
    window show
    with Dissolve(1.0)
    pause 0.5
    pov "胃癌，我知道这是什么意思。"
    pov "就算去最好的医院，买最贵的药，也不过多苟延残喘几天。"
    pov "更何况，我的存款早就开始见底了。"
    pov "与其孤独地死在出租屋里，还不如现在就从这里跳下去。"
    pov "至少，还能够早点解脱。"
    pause 1.0
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
    pause 1.0  
    play sound "audio/sfx/sfx_001.mp3" volume 0.3
    unknown "喂，你在做什么呢？"
    pov "突如其来的声音将我吓了一跳。"   
    pov "转过头，只见身后不知何时站着一名少女。"
    play music "audio/bgm/BGM_002.mp3" volume 0.5
    show you dress normal 1 with Dissolve(1.0)
    

    #7
    window show
    with dissolve
    pause 0.5 
    pov "......"
    pov "是同一间病房的人。"
    pov "虽然基本没在病房里待过，但因为长得很漂亮，让我对她有点印象。"
    pov "不过，漂亮与否和我没有关系，突然闯入的陌生人只会让我感到不快而已。"

    #8
    unknown "站那儿可是很危险的，快下来吧。"
    unknown "还是说......你想要跳下去？"
    unknown "啊，那是你的诊断书吗？我能看看吗？"
    show you at yuu_updown(0.3,935)
    pause 0.5
    pov "我还没来得及说话，她就自顾自地捡起被扔在地上的诊断书。"

    unknown "喔喔，胃癌啊，年纪轻轻的还真是不走运。"
    unknown "......"
    unknown "你该不会......是因为这个才想自杀吧？"
    unknown ".{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}."
    unknown "真的假的？"
    unknown "再考虑一下比较好哦？父母可是会伤心的。"
    
    #9
    yin "父母早就......."
    pov "说到一半，我才意识到没有必要和她白费口舌，于是狠狠瞪了过去。"
    yin "话说和你没关系吧！你谁啊？"
    unknown "啊哈哈，别露出那么可怕的表情嘛。"
    unknown "而且，什么叫没关系，面前可是有一个活生生的人想要跳楼哦？"
    unknown "再怎么说也没办法做到假装看不见吧。"
    yin "什么意思，难道你想阻止我吗？"
    
    #10

    stop music fadeout 2.0
    play sound "audio/sfx/sfx_001.mp3" volume 0.3
    pov "胸口生出一股无名的怒火。"
    pov "身体因为愤怒而发抖，我忍不住攥紧了拳头。"
    play sound "audio/sfx/sfx_003.mp3"
    yin "{size=+2}你以为你是谁啊？{w=0.2}少在那儿装好人了，你懂我的什么？{w=0.4}{nw}{/size}" with vpunch
    extend "\n{size=+4}亲人全死光了什么感受你知道吗！？{w=0.4}{nw}{/size}" with hpunch
    extend "\n什么都不懂的家伙就别在那儿装模做样彰显同情心了！" with hpunch

    pov "我对着她破口大骂起来。"
    scene black with Dissolve(1.0)
    pause 2.0 

    pov "其实我知道的，我只是不讲理地将怨气发泄在她的身上而已。"
    pov "或许她和周围的人一样，只是想在力所能及的范围内安慰我一下，并没有别的意思。"
    pov "可是，我实在是没心情去顾及她的感受了。"
    pov "我只想安安静静去死而已。"
    play sound "audio/sfx/sfx_001.mp3" volume 0.2
    scene bg rooftop cloudy with Dissolve(1.5)
    show you dress normal 1 with Dissolve(0.5)
    pause 0.5 
    pov "......"
    show layer master:
        xalign 0.5 yalign 0.5
        zoom 1.5 yoffset 200  
        ease 3 xoffset -50
    with Dissolve(0.5)        
    pause 1.5
    pov "不过，出人意料的是，面对我的怒吼，她并没有露出害怕的表情。"
    pause 0.5
    show layer master:
        zoom 1.0 
        xoffset 0 yoffset 0
        xalign 0.0 yalign 0.0 
    with Dissolve(0.5)

    #11
    pause 1.0 
    play music "audio/bgm/BGM_002.mp3" fadein 1.0 volume 0.5
    unknown "你好像搞错了点什么，我可没有阻止你的想法。"
    unknown "你连死都不怕，还有谁能拦得住你。"
    unknown "我只是觉得，有点可惜而已。"
    yin "......哈？"
    unknown "毕竟你看，咱们都是女孩子，就算死，也要死的漂亮一点吧？"
    unknown "从这里跳下去的话，你全身的骨头会摔得粉碎，四肢会像蜈蚣一样弯曲成一个好笑的角度。"
    unknown "如果运气差点脑袋着地，那就更惨了，红的白的直接撒一地。"
    unknown "唉......我是想不出有什么死法比摔死更惨烈了。"
    yin "......"
    pov "背后起了一阵鸡皮疙瘩。"
    camera:
        yoffset 10
        linear 0.03 yoffset 10
        linear 0.03 yoffset -10
        linear 0.03 yoffset 8
        linear 0.03 yoffset -8
        linear 0.03 yoffset 4
        linear 0.03 yoffset -4
        linear 0.03 yoffset 0  
    pause 1.0 
    pov "我咽了口口水，下意识后退几步。"
    
    #12
    unknown "而且吧，你要是从这儿跳下去，自己死了不说，还得添一堆麻烦。"
    unknown "替你收尸的那人肯定会捏着鼻子，心想今天怎么这么倒霉。"
    unknown "对了，还有这里的院长，就是戴黑框眼镜的那个秃顶大叔。"
    unknown "人家才刚上任几年，你就来这么一出，估计他最后那点头发也要掉光了。"
    unknown "不过要说最困扰的人还是我啦。"
    unknown "因为天台的门是我偷偷打开的，来这里看风景可是我为数不多的兴趣了。"
    unknown "你要是死了，追查起责任，肯定还得算到我头上......"

    show layer master:
        xalign 0.5 yalign 0.5
        zoom 1.5 yoffset 200  
        linear 20 xoffset -100
    with Dissolve(1.0) 
    pause 1.0  
    pov "......"
    pov "人不可貌相。"
    pov "看着滔滔不绝的少女，我深刻理解了这句话的含义。"
    pause 1.0 
    pov "从某种别的意义上。"
    pause 1.0  
    pov "我还从来没见过如此讨厌的家伙。"
    pov "面对寻死之人，她竟然还能拿那种无所谓的态度来开玩笑。"
    pov "有一瞬间，我甚至生出了要拉着她一起跳下去的阴暗念头。"
    stop music fadeout(3.0)
    scene black with Dissolve(1.0)
    pause 1.0 
    pov "但是不可否认，她说的有几分道理。"
    pov "我活在这个世界上本来就祸害了不少人，如果死了还要继续添麻烦，实在说不过去。"
    pov "还是找个没人的地方去死吧......"
    pov "这么想着，我从天台边上退了下来。"
    scene bg rooftop cloudy with Dissolve(1.0)
    show you dress normal 1 with Dissolve(0.5)
    window show dissolve
    pause 0.5
    unknown "你决定下来了吗？真是太感谢了！"
    show you at yuu_updown(0.3,925)
    unknown "给，你的诊断书。"
    play sound "audio/sfx/sfx_004.mp3" fadeout 1.0
    pause 1.0 
    camera:
        xoffset 10
        linear 0.03 xoffset 10
        linear 0.03 xoffset -10
        linear 0.03 xoffset 8
        linear 0.03 xoffset -8
        linear 0.03 xoffset 4
        linear 0.03 xoffset -4
        linear 0.03 xoffset 0
    pause 1.0 
    pov "我一把抢过诊断书，揉成一团，用力丢了出去。" 
    pov "少女和诊断书都是令人讨厌的存在，如果可以，我真希望再也不要见到她们。"
    scene black with Dissolve(1.0)
    window hide
    pause 1.0
    pov "然而......"
    $ renpy.pause(1.0, hard=True)
    play sound "audio/sfx/sfx_005.mp3" volume 0.8 
    $ renpy.pause(2.0, hard=True)
    play music "audio/bgm/bgm_003.mp3" volume 0.8 
    pause 0.5


    show cg 1 cloudy normal 3840 as closeup:
        subpixel True 
        zoom 1.0
        xalign 1.0 yalign -0.01 
        alpha 0.0            
        parallel:
            linear 2.0 alpha 1.0
        parallel:
            pause 1.0 
            ease 6.0 xalign 0.7 yalign 0.05
    
    $ renpy.pause(7.0, hard=True)

    show cg 1 cloudy normal 1920 as fullview:
        subpixel True
        xalign 0.5 yalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0 
    hide closeup with Dissolve(1.0)
    pause 1.5
    window show dissolve
    pause 0.5
    
    pov "少女依然站在原地，完全没有离开的意思。"
    unknown "请等一下。"
    yin "干什么？快让开！"
    pov "我换上最强硬的语气，试图将她赶走，可是她却一点也不在意。"
    unknown "嘻嘻，你别着急，先听我说完嘛。"
    unknown "你知道这么一个传闻吗？"
    unknown "听说，如果一个人的命运特别悲惨，神明出于怜悯，就会派出天使，在生命的最后帮助她实现愿望。"
    yin "你有毛病吧？谁会信这种鬼话？"
    pause 0.5
    pov "世界上根本就没有什么神明，也没有什么天使。"
    pov "要是那种东西真的存在的话，爸爸妈妈，还有祖母就不会死了......"
    camera:
        xoffset 10
        linear 0.03 xoffset 10
        linear 0.03 xoffset -10
        linear 0.03 xoffset 8
        linear 0.03 xoffset -8
        linear 0.03 xoffset 4
        linear 0.03 xoffset -4
        linear 0.03 xoffset 0
    pause 1.0 
    yin "总之快给我让开！"
    pov "伸出手，我想将她推开。"
    pov "可是，做到一半的动作却突然停住了。"
    pause 1.0
    unknown "其实，传闻是真的。"
    window hide Dissolve(1.0) 

    show cg 1 shine normal 1920 as fullview with Dissolve(1.5)
    

    pause 1.0
    window show dissolve
    pause 0.5
    pov "飞鸟掠过上空，少女的发丝和裙摆在空中飘动。"
    pov "阳光穿过厚重的云层，洒落在她的身上，朦胧中仿佛添上了一双翅膀。"
    pause 0.5
    pov "少女的脸上露出前所未有的甜美笑容，我不由得愣在原地。"

    pause 1.5
    unknown "因为，我就是那个派来帮助你的天使。"

    scene black with Dissolve(1.5)
    stop music fadeout 3.0

    pov"test"