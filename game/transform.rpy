# 小林悠的立绘定义
# transform yousize:
#     zoom 0.8
#     xalign 0.5
#     yalign 1.0
#     yoffset 900


#小林悠的上下晃动特效
transform yuu_updown(t=0.5, target_y=935):
    yousize                  # 依然死死继承尺寸和对齐，保证人绝对不飞
    linear t yoffset target_y # 使用你传入的时间和位置，匀速慢速下沉
    linear t yoffset 900     # 再用一模一样的时间，精准慢速回弹到 900 原位