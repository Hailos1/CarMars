screen ctc(arg=None):

    zorder 100

    hbox:
        xalign 0.96
        yalign 0.96
        spacing 10
    

transform ctc_animation:
    parallel:
        alpha .2
        linear 1.0 alpha .9
        linear 1.0 alpha .2
        repeat
    parallel:
        linear 0.3 yoffset 0
        linear 0.3 yoffset 10
        linear 0.3 yoffset 0
        linear 0.3 yoffset -10
        repeat