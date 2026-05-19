#game/definitions.rpy
# 定义人物
transform yousize:
    zoom 0.8
    xalign 0.5      # x line
    yalign 1.0      # y line
    yoffset 900


define config.tag_transform = {
    "you": yousize
}

define lin = Character(_("【小林悠】"), color = "#ffffff", image = "you")

define yin = Character(_("【月宫夏音】"), color = "#ffffff")

define pov = Character(None)

define p_nvl = Character(None, kind=nvl)

define unkown = Character(_("? ? ?"), color = "#ffffff")

#定义文字在正中间的函数
init -1:
    screen intro_text_screen(my_text):

        vbox:
            xalign 0.5         
            yalign 0.5         
            
            text my_text:
                size 38            
                color "#ffffff"    
                xalign 0.5        
                text_align 0.5    


#定义NVL的文字位置
style nvl_window:
    top_padding 150       # 只有顶部往下踩 350 像素
    bottom_padding 100    # 底部依然留足空间，让文字能继续往下码