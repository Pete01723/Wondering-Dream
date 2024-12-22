label start:
    scene bg room1
    with dissolve_scene_full

    "You suddenly woke up when you heard your mother screaming at you."

    show mom 2

    mom "Hoy! you wake up late again!?"

    mc "Mmm... Mom?"

    mom "Stop slacking and gather some woods in the forest for laters lunch cooking. We are already running out of firewood."

    if badend2:
        mc "..."

        scene black
        with dissolve_scene_full

        "End"

        return

    menu:
        "Alright, I’m on it mom… Jeez.":
            pass

        "You ignore your mom and continue to sleep in your bed.":
            scene black

            "You continue to sleep in your bed as you still feel sleepy."

            scene bg room2
            show momsplash
            with hpunch
            play sound "sfx/water_splash.mp3"

            "Later, your mother suddenly  splashes your face with water."

            mc "WAAAAAAH- MOM!!!"

            hide momsplash
            show mom 2

            mom "Wake up already! Tidy yourself now! We Don't have all day!"

    mc "Alright mom, I’m on it!…Jeez."

    "You change and prepare yourself, A little bit of warm up and you grab your axe and your sack."

    mc "Mom! I'm going now, I’ll be back around 11."

    show mom 1

    mom "Take care! Don't get lost on your way or you will never go back home."

    mc "Yeah, yeah.. I know that already.. You don’t have to say it a couple of times."

    mom "I’m just only reminding you anak."

    "You ignore your mom's words before you go."

    hide mom
    jump chap1

label chap1:
    scene bg forest1
    with dissolve_scene_full

    "You are on your way to the forest."

    "When you suddenly stumble across a somewhat weird entrance-like in the forest."

    scene bg forest_hole
    with dissolve_scene_half

    mc "What is that?"

    mc "I’ve never seen anything like that before?"

    "Suddenly you hear a whisper."

    "???" "Get inside"

    mc "Huh?"

    mc "Who is that? Someone there?"

    "You look around but there is no one around."

    mc "I guess it was my thoughts."

    "You stare again at the arch and curious what’s inside since you have never seen anything like that before…"

    menu:
        "Should I go?"

        "No":
            "You decided not to go inside but when you were about to continue your journey, suddenly your path was gone as it never existed."

            scene bg forest2

            mc "Huh? Where am I? Where’s my path"

            scene bg forest_hole

            "You look around and you are surrounded by trees, only you and the entrance."

            mc "I guess I have no choice then."
        
        "Yes":
            pass

    scene bg forest_hole

    "Out of your curiosity, you go inside"

    scene bg loop

    "As you go inside, your walks are getting deeper and deeper."

    "Slowly, the world around you changes as you are in a different world."

    "Suddenly,  you fainted."

    scene black
    with dissolve_scene_full

    "..."

    scene bg forest_day
    with dissolve_scene_full

    "You woke up in the middle of the forest."

    mc "Huh? Where am I?"

    "You are amazed and confused as to why the world here is different here from yours."

    "You wander around by amazement and hoping you can get back from home."

    "Few hours goes by, you are still in this place as if you are in a loop."

    mc "*sigh*"

    mc "How am I still here? It's like forever…"

    mc "I wish I could go back home."

    play sound "sfx/rustle_bush.mp3"

    "*rustle*"

    mc "Huh? What is that?"

    play sound "sfx/rustle_bush.mp3"

    "*rustle*"
    
    "You hold a nearby stick in the ground and you slowly approach the rustling bush"

    play sound "sfx/rustle_bush.mp3"

    "*rustle*"

    show cat 1 at h11
    play sound "sfx/cat_meow.mp3"

    "Suddenly, a cat jumps out of the bush"

    mc "Phew.. It’s just a cat."

    "The cat walks towards you and swirls around your feet."

    mc "Hello there kitty…"

    show cat 2

    "You find the cat very cute so  you pet it."

    mc "Aren’t you an adorable little kitty?"

    menu:
        "As you pet it, the cat slowly walks and looks back at you as it wants you to follow her."

        "Follow it":
            pass

        "Catch it and continue to pet":
            "You catch her off guard and continue to pet her"

            show cat 3
            play sound "<to 2>sfx/cat_hissing.mp3"

            "but the cat instead got irritated and almost bit your hand."     

            mc "Ow!"

            hide cat

            "At the same time, it escapes from your gasp and runs away until it disappears into your gaze."

            "You feel bad for the cat and continue to wander around the woods hoping for a way to escape."

            jump badend

    show cat 1

    "You follow the cat as it knows where it's going."

    play sound "sfx/rustle_bush.mp3"

    "A minute later, the cat stops and hides in the bush."

    hide cat

    mc "Hey wait-"

    show myst 1

    $ m_name = "???"

    m "Hello there."

    mc "H-hello. W-who are you?"

    show myst 2

    m "How did you get into this world?"

    mc "Huh?"

    show myst 3

    m "Leave now or the shadow will hunt you."

    mc "Who?"

    show myst 1

    m "The one that brought you here and eats you alive."

    mc "How do I know what you are saying is true?"

    m "Because it was my child"

    "You suddenly feel uneasy by his words and having a second thoughts"

    show myst 2

    menu:
        m "..."

        "Don't trust her":
            $ badend2 = True

            show myst 1

            m "Are you going to leave or not?"

            mc "I will but not under your guidance."

            show myst 3

            m "Goodluck then"

            hide myst

            "You continue to walk away from her and continue your journey on looking for home."

            show cat 1

            "The cat sneakily followed you but you didn’t notice."

            hide cat

            jump badend

        "Trust Her":
            show myst 1

            m "I won’t and I will help you."

            m "Follow the cat and you will have your way back."

            mc "Thank you"

            m "Be Careful."

            hide myst

            show cat 1
            play sound "sfx/cat_meow.mp3"

            "You follow her as it leads you deep into the forest."

            scene bg old_tree

            "Few minutes later, You and the cat arrive in front of a giant old tree and in its roots there is a door-like."

            "The cat stops and looks like it gives you a sign to get inside."

            mc "Thank you."

            show cat 2
            play sound "sfx/cat_meow.mp3"

            "The cat suddenly runs to your feet in circles as it purrs."

            mc "I’m going to miss you."

            hide cat

            "You enter the big tree and you continue to walk inside."

            scene bg loop_light
            play sound "<loop 1>sfx/loophole.mp3"

            "As you walk deeper and deeper, you saw a light"

            "As soon as you see it you run towards it."

            stop sound
            scene bg forest1
            with dissolve_scene_full_white

            "As you enter the light, you realize you are back in the same forest."

            mc "Finally, I’m back"

            play sound "sfx/running_forest.mp3"

            "You run and head home as soon as possible."

            "You never look back and you will never ever go back to that place again."

            stop sound
            scene black
            with dissolve_scene_full

            "Good End"

            return
            
label badend:   
    scene bg forest_night
    with dissolve_scene_full

    "The night falls and you still haven't found your way home."

    "You continue to walk and suddenly"

    show monsshadow

    "you notice someone is standing in the distance."

    "A sigh of relief as it was the only ticket to get out of the forest."

    hide monsshadow

    play sound "<loop>sfx/running_forest.mp3"

    "You shout as you run towards that person."

    mc "Hey you there! I need some help, I’m lost. Do you know the way out?"

    "As you run closer to that person you notice something is different from it."

    "It's not moving nor talking."

    mc "Hey!"

    "As you approach, the moonlight reveals that it is not a person…"

    stop sound

    mc "Oh no."

    show mons 1 

    "but a monster."

    play sound "<from 0.75 to 1.75>sfx/ground_fall.mp3"

    "Out of fear, you fell to the ground as the monster got closer and stared at you."

    mons "Hello there little fella."

    mc "S-stay away f-from me"

    "You try to stand up to run away but-"

    show mons 2

    mons "You can’t run away"

    mons "I brought you here"

    if badend2:
        hide mons
        show monschoke

        "The monster picks you up by his deadly large claws"

        mc "Put me down, put me down!"

        "You try to escape his grasp but he is too powerful"

        mons "*Chuckles*"

        mons "You have no escape from-"

        hide monschoke
        show mons 3 at t21
        show cat 3 at t22

        "Suddenly a cat jumps out and bites its hand protecting you."

        show mons 4 at t21

        mons "What the-"

        play sound "<to 2>sfx/cat_hissing.mp3"

        c "*Hiss*"

        c "Leave him alone!"

        mc "Y-you"

        c "Get away from here!"

        show mons 3
        with hpunch
        play sound "<to 3.50>sfx/mons_scream.mp3"

        menu:
            mons "RAAAAAAAAAAAAAAAGHH!!!!"

            "Stay and Help her.":
                mc "No, I will Help."

                c "No, Stay away-"

                mons "You cannot stop me mother."

                hide cat
                hide mons

                show monschoke
                with hpunch

                "The monster suddenly overthrow her mother and suddenly grabs you"

                mons "You are MINE!"

                hide monschoke
                show monsscare2

                $ pause(3)

                hide monsscare2

                scene black
                with dissolve_scene_full

                "Bad Ending"

                return

            "Run":
                hide mons
                hide cat

                "You run as fast as you can."

                scene bg old_tree

                "Suddenly, you see an old tree with an entrance like inside."

                "Without hesitation you enter it."

                scene bg loop
                play sound "<loop 1>sfx/loophole.mp3"

                "As you run inside, it's getting deeper and deeper."

                "Slowly, the world around you changes as you are in ???"

                "Suddenly, you fainted."

                stop sound

                jump start

    "You slowly backs away as you look at him in fear"

    mc "G-go away, go away!"

    "You try to escape but you are fully consumed by fear."

    mons "*Chuckles*"

    show mons 3

    mons "You have no escape-"

    mons "FROM ME!"

    show monsscare1

    $ pause(3)

    hide monsscare1
    hide mons

    scene black
    with dissolve_scene_full

    "Bad Ending"

    return