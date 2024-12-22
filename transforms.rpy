transform tcommon(x=960, z=1):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=960, z=1):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform sink(x=960, z=1):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

transform hop(x=960, z=1):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform thide(z=1):
    subpixel True
    transform_anchor True
    on hide:
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20

transform t41:
    tcommon(300)
transform t42:
    tcommon(739)
transform t43:
    tcommon(1179)
transform t44:
    tcommon(1620)
transform t31:
    tcommon(360)
transform t32:
    tcommon(960)
transform t33:
    tcommon(1560)
transform t21:
    tcommon(600)
transform t22:
    tcommon(1320)
transform t11:
    tcommon(960)

transform i41:
    tinstant(300)
transform i42:
    tinstant(739)
transform i43:
    tinstant(1179)
transform i44:
    tinstant(1620)
transform i31:
    tinstant(360)
transform i32:
    tinstant(960)
transform i33:
    tinstant(1560)
transform i21:
    tinstant(600)
transform i22:
    tinstant(1320)
transform i11:
    tinstant(960)

transform h41:
    hop(300)
transform h42:
    hop(739)
transform h43:
    hop(1179)
transform h44:
    hop(1620)
transform h31:
    hop(360)
transform h32:
    hop(960)
transform h33:
    hop(1560)
transform h21:
    hop(600)
transform h22:
    hop(1320)
transform h11:
    hop(960)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat

define dissolve = Dissolve(0.25)
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)