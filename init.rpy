image bg woods_day = 'bg/woods_day.png'
image bg woods_night = 'bg/woods_night.png'
image bg cave_out = 'bg/cave_out.png'
image bg cave_ins = 'bg/cave_ins.png'
image bg house = 'bg/room.png'
image black = "#000000"

image cat 1 = Composite((1920, 1080), (0, 0), "cat/cat_base.png", (0, 0), "cat/cat_neutral.png")
image cat 2 = Composite((1920, 1080), (0, 0), "cat/cat_base.png", (0, 0), "cat/cat_happy.png")
image cat 3 = Composite((1920, 1080), (0, 0), "cat/cat_base.png", (0, 0), "cat/cat_angry.png")

image myst 1 = Composite((1920, 1080), (0, 0), "myst/myst_base.png", (0, 0), "myst/myst_neutral.png")
image myst 2 = Composite((1920, 1080), (0, 0), "myst/myst_base.png", (0, 0), "myst/myst_curious.png")
image myst 3 = Composite((1920, 1080), (0, 0), "myst/myst_base.png", (0, 0), "myst/myst_angry.png")

image mons 1 = Composite((1920, 1080), (0, 0), "mons/mons_base.png", (0, 0), "mons/mons_neutral.png")
image mons 2 = Composite((1920, 1080), (0, 0), "mons/mons_base.png", (0, 0), "mons/mons_smile.png")
image mons 3 = Composite((1920, 1080), (0, 0), "mons/mons_base.png", (0, 0), "mons/mons_run.png")
image monsscare = "mons/mons_scare.png"
image monsshadow = "mons/mons_shadow.png"

define mc = Character('You', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '')
define m = Character('m_name', image = 'myst', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '', dynamic = True)
define c = Character('cat_name', image = 'cat', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '', dynamic = True)
define mons = Character('mons_name', image = 'mons', what_prefix = '"', what_suffix = '"', ctc = 'ctc', ctc_position = '', dynamic = True)

define m_name = "Myst"
define cat_name = "Cat"
define mons_name = "Monster"