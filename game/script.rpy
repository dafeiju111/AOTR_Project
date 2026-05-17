# 游戏的脚本可置于此文件中。

# 游戏在此开始。

label start:
    stop music fadeout 1.5
    scene black with dissolve
    $ renpy.block_rollback()

    jump chapter_1_start
    return
