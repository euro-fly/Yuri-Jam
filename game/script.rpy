# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:

    image computerroom = Image("images/bg/ComputerRoom.png")
    image rooftop = Image("images/bg/Rooftop.png")

    transform transpa:

        alpha 0.5

    python hide:

        def gen_randmotion(count, dist, delay):

            import random

            args = [ ]

            for i in range(0, count):
                args.append(anim.State(i, None,
                                       Position(xpos=random.randrange(-dist, dist),
                                                ypos=random.randrange(-dist, dist),
                                                xanchor='left',
                                                yanchor='top',
                                                )))

            for i in range(0, count):
                for j in range(0, count):

                    if i == j:
                        continue

                    args.append(anim.Edge(i, delay, j, MoveTransition(delay)))

            return anim.SMAnimation(0, *args)

        store.randmotion = gen_randmotion(5, 7, 1.0)


init python:

    def double_vision_on(picture):

        renpy.scene()

        renpy.show(picture)

        renpy.show(picture, at_list=[transpa,randmotion], tag="blur_image")

        renpy.with_statement(dissolve)


    def double_vision_off():

        renpy.hide("blur_image")

        renpy.with_statement(dissolve)

# Declare characters used by this game.
define s = Character('Stray', color="#c8ffc8")

define k = Character('Kitsune', color="#c8f4ff")

image phone = "images/phone/bustedphone.png"
image bgphone = "images/phone/phone-def.png"
image bg wasteland = "images/wasteland.jpg"
image bg wip = "images/bg/bg wip.png"
image bg computerroom = "images/bg/ComputerRoom.png"
image bg computerblur = "images/bg/ComputerRoom-blur.png"
image bg rooftop = "images/bg/Rooftop.png"
image bg rooftopblur = "images/bg/Rooftop-blur.png"
image eileen normal = "images/sylvie_normal.png"
image eileen giggle = "images/sylvie_giggle.png"
image eileen smile = "images/sylvie_smile.png"
image eileen surprised = "images/sylvie_surprised.png"

image stray normal = "images/sprites/stra-default.png"
image stray upset = "images/sprites/stra-upset.png"
image stray embarrassed = "images/sprites/stra-emba.png"
image stray frown = "images/sprites/stra-frown.png"
image stray talk = "images/sprites/stra-open-default.png"
image stray blush = "images/sprites/stra-smileblsh.png"
image stray smile = "images/sprites/stra-smilepng.png"

image kitsune normal = "images/sprites/kit_default_phone.png"
image kitsune baited = "images/sprites/kit_baited_phone.png"
image kitsune smile = "images/sprites/kit_smile_phone.png"
image kitsune smug = "images/sprites/kit_smug_phone.png"
image kitsune talk = "images/sprites/kit_talk_phone.png"



# Picking up the phone
transform phone_pickup:
    yalign 1.0 xalign 0.5
    yoffset 550
    easein 0.3 yoffset 140
    on hide:
        easeout 0.2 yoffset 600

transform phone_message_bubble_tip:
    xoffset 10
    yoffset 1
    
transform phone_message_bubble_tip2:
    xoffset 165
    yoffset 1

transform phone_message_bubble_tip3:
    xoffset 120
    yoffset 1

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0
        
transform incoming_message:
    yoffset 300
    xoffset 10
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0
    on hide:
        scrolling_out_message
        
transform midleft:
  xpos 0.2
  yalign 1.0
  
transform midright:
  xpos 0.5
  yalign 1.0

# The game starts here.
label start:
    
    play music "bgm/main stay.mp3"
    
    scene bg computerroom
    with fade
    
    $ renpy.pause(0.5)
    scene bg computerblur

    $ double_vision_on("computerroom")
    $ renpy.pause(0.2)

    show bgphone at left
    with dissolve 
    ## Add cellphone screen here
    $ renpy.pause(0.5)
    show phone at phone_pickup
    with dissolve
    $ renpy.pause()
    play sound "sfx/blop.mp3"
    show screen phone_message_system("#monitors: survivors chatroom for general bullshit")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("You have now joined #monitors as *Stray.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("*Kitsune has entered #monitors.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Hey")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("How's it going?")
    $renpy.pause()
    hide screen phone_message_me
    
    hide screen phone_sticker_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Hey hey~")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Just got up.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Same")
    $ renpy.pause()
    hide screen phone_message_me
    show screen phone_message_me("Let's see how fucked we are today.")
    $ renpy.pause(0.5)
    call screen phone_reply("!todaystatus", "notajump")
    
    label notajump:
    hide screen phone_message_me
    $ renpy.pause(0.5)
    play sound "sfx/blop.mp3"
    show screen phone_message_system("Current temperature: 61F/16C. Cloudy with possible showers.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("Headline #6661: Year Five of the ongoing Omen crisis. Situation still grave, as usual. No progress on a cure.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("Attack reported in California at 1300 hours, with 10 reported casualties.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("Refer to !pop for current population data.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Looking grim~")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("tell me something I don't know.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "wow, someone's full of sunshine today.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "feeling lonely?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("oh shut up.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "sowwy~")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "well if it makes you feel any better")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "while hanging around uncharted territory near my place yesterday")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "i found an empty home")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "WITH UNTOUCHED SNACKS")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("AAAAAAA")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "yep!!")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_sticker_other("Kitsune", "chips")
    $ renpy.pause()
    hide screen phone_sticker_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "just to make you jealous.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "i had no idea salty chips could ever taste so sweet.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "funyuns, BBQ chips, the works.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("haha i could certainly go for chips right now")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("haven't had some in years, son of a gun")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "is the gun fully-automatic, at least~?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("...")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "but on a serious note i found some bottled water")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "which is always nice")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "and... a ton of those CDs you'd probably like i think")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Hm?")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "oh, mostly jazz stuff")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "at least i think it's jazz.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_sticker_other("Kitsune", "jazz")
    $ renpy.pause()
    hide screen phone_sticker_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "like, we've got... one of em was by Miles something or other.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "then you had the... cannon ball?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "don't look at me, i'm not like, an expert")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "it seemed like it was your kinda thing is all")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Yeah yeah.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "How are things on your end?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Hmm")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Went up top today to do a surveillance sweep, all clear so far.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Weather is *still* foggy as shit.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Omens are gathering in the usual spots, so I picked a number of them off today.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "My hard little worker~")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me(">_>")

    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_system("*Ohms has entered #monitors.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Oh hey Ohms! o/")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("yo")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "You kids. Flirting while I'm not around.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("uuuuuugh")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "hahahahaha")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "Anyways")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "how goes it?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Oh, Stray here was just telling me of her heroic tales")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Killing Omens left and right on surveillance duty")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "my hero~")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Save me.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "lol. your problem not mine.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("...")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("how have you been, ohms?")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "eh, same old same old")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "stayed holed-up. played some net games.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "just shut-in things.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "I should prob go out and stretch my legs, do some killing.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "But. You know how it is where I am.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("mm.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "er")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "doing okay there, stray?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("oh")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("my bad. kit was just showing off her snack haul.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("I'm still salty. goddamn.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "oh what")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "lmao I see it")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "daaaaaamn. funyuns, too?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "damn straight!")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "eyyyyy")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("...")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("I hope they're SOGGY AS SHIT.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "wow rude")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "^")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "but that aside. how goes surveillance, Stray? going out again today?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("yeah. most likely.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("the west wing still needs to be secured.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "sounds rough.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("eh. it is what it is.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "not just strong, but humble too~ what a hero.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me(">________>")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "ah, yes. this is what i am here for.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Ugh not you too?")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "hey, look man")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "it's not like I have anything better to do")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "Kitsune- oh btw")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "what's up?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "event's up. how far have you gotten?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "OH")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Shit, that's TODAY?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "yep.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "better get your ass back in grinding hell if you wanna catch up")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "FFFFFFFFFfffffff")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "fffffff")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "fff")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Yeah no")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("I don't think I will ever understand how you guys are STILL playing that game despite the apocalypse")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "IT'S WHAT I LIVE FOR.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "SAME.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("You two are such millennials.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "omg look who's talking")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Look, you could play so many other games")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_sticker_me("ps2")
    $ renpy.pause()
    hide screen phone_sticker_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("There's a working PS2 and a backlog to last you DAYS")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "zzzz")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "straaaaaay")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "joiiiiiiin ussssss")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Pass.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", ":'(")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "rip")




    $ renpy.pause()

    hide screen phone_message_other
    hide phone

    $renpy.pause(0.2)
    jump continues    
        
##Hide cellphone screen

    
    
label continues:
    window show
    s "My mom is great."
    return 