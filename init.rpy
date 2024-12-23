init python:
    def pause(time=None):
        global _windows_hidden

        if not time:
            _windows_hidden = True

            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)

            _windows_hidden = False

            return

        if time <= 0:
            return

        _windows_hidden = True

        renpy.pause(time)

        _windows_hidden = False

define audio.rlroom = "<loop 0>bgm/roomrl.mp3"
define audio.foresthole = "<loop 0>bgm/foresthole.mp3"
define audio.forest = "<loop 3>bgm/forest.mp3"
define audio.forestnight = "bgm/nightforest_scene2.mp3"
define audio.run = "<loop 1>bgm/run.mp3"
define audio.myst = "bgm/myst_scenes.mp3"
define audio.goodend = "bgm/good_ending.mp3"

image bg room1 = 'bg/room_rl.png'
image bg forest_day = 'bg/forest_day.png'
image bg forest_night = 'bg/forest_night.png'
image bg forest1 = 'bg/forest_rl1.png'
image bg forest2 = 'bg/forest_rl2.png'
image bg forest_hole = 'bg/foresthole_rl.png'
image bg loop = 'bg/loophole_1.png'
image bg loop_light = 'bg/loophole_2.png'
image bg old_tree = 'bg/old_tree.png'
image bg ending1 = 'bg/ending_1.png'
image bg ending2 = 'bg/ending_2.png'
image bg ending3 = 'bg/ending_3.png'
image bg ending4 = 'bg/ending_4.png'

image black = "#000000"

image cat 1 = Composite((1920, 1080), (0, 0), "cat/cat_base.png", (0, 0), "cat/cat_neutral.png")
image cat 2 = Composite((1920, 1080), (0, 0), "cat/cat_base.png", (0, 0), "cat/cat_happy.png")
image cat 3 = Composite((1920, 1080), (0, 0), "cat/cat_base.png", (0, 0), "cat/cat_angry.png")

image myst 1 = Composite((1920, 1080), (0, 0), "myst/myst_base.png", (0, 0), "myst/myst_neutral.png")
image myst 2 = Composite((1920, 1080), (0, 0), "myst/myst_base.png", (0, 0), "myst/myst_curious.png")
image myst 3 = Composite((1920, 1080), (0, 0), "myst/myst_base.png", (0, 0), "myst/myst_angry.png")

image mons 1 = Composite((1920, 1080), (0, 0), "mons/mons_base.png", (0, 0), "mons/mons_neutral.png")
image mons 2 = Composite((1920, 1080), (0, 0), "mons/mons_base.png", (0, 0), "mons/mons_smile.png")
image mons 3 = Composite((1920, 1080), (0, 0), "mons/mons_base.png", (0, 0), "mons/mons_claw.png")
image mons 4 = Composite((1920, 1080), (0, 0), "mons/mons_base.png", (0, 0), "mons/mons_neuclaw.png")
image monsscare1 = "mons/mons_scare1.png"
image monsscare2 = "mons/mons_scare2.png"
image monsshadow = "mons/mons_shadow.png"
image monschoke = "mons/mons_choke.png"

image mom 1 = "mother/mother_neutral.png"
image mom 2 = "mother/mother_angry.png"
image momsplash = "mother/mother_splash.png"

define mc = Character('You', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '')
define m = Character('m_name', image = 'myst', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '', dynamic = True, who_color = "#7348e9")
define c = Character('cat_name', image = 'cat', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '', dynamic = True, who_color = "#7348e9")
define mons = Character('mons_name', image = 'mons', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '', dynamic = True, who_color = "#db0000")
define mom = Character('mom_name', image = 'mom', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '', dynamic = True, who_color = "#ee853f")

define m_name = "Myst"
define cat_name = "Cat"
define mons_name = "Monster"
define mom_name = "Mother"

define badend2 = False

