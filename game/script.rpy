# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    image computerroom = Image("images/bg/ComputerRoom.png")
    image rooftop = Image("images/bg/Rooftop.png")
    image zombies = Image("images/scenes/zombies_default.png")
    image zombiesblood = Image("images/scenes/zombies_blood.png")
    image moment = Image("images/scenes/moment.png")
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

define narrator = nvl_narrator

image phone = "images/phone/bustedphone.png"
image chatphone = "images/phone/phone-def.png"
image lockphone = "images/phone/phone-default.png"
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
image stray uniform = "images/sprites/stra-uniform.png"

image kitsune normal = "images/sprites/kit_default_phone.png"
image kitsune baited = "images/sprites/kit_baited_phone.png"
image kitsune smile = "images/sprites/kit_smile_phone.png"
image kitsune smug = "images/sprites/kit_smug_phone.png"
image kitsune talk = "images/sprites/kit_talk_phone.png"

image bg zombies = "images/scenes/zombies_default.png"
image bg zombiesblood = "images/scenes/zombies_blood.png"
image bg moment = "images/scenes/moment.png"
image bg snipe = "images/scenes/snipe.png"



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
  yalign 1.

label message(who, what):
    $ renpy.pause()
    hide screen phone_message_other
    hide screen phone_message_me
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    if who == "Stray":
        show screen phone_message_me(what)
    elif who == "System"
        show screen phone_message_system(what)
    elif who != "":
        show screen phone_message_other(who, what)
    return

# The game starts here.
label start:
    
    play music "bgm/main stay.mp3"
    
    scene bg computerroom
    with fade
    
    $ renpy.pause(0.5)

    $ double_vision_on("computerroom")
    $ renpy.pause(0.5)


    "Sun - Oct. 19 - 13:00"

    nvl clear
    window hide

    show chatphone at left
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
    show screen phone_message_system("Current Topic: Welcome to the end of the world!")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("You have now joined #monitors as @Stray.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("@Kitsune has entered #monitors.")
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
    play sound "sfx/blop.mp3"
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
    show screen phone_message_system("Attack reported in California at 1300 hours, with 10 dead.")
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
    show screen phone_message_other("Kitsune", "hmm")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "well if it makes you feel any better")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "I mapped out some of the uncharted waters around my place")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "found an empty home")
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
    show screen phone_message_other("Kitsune", "found a can of pringles, but i've also got funyuns, BBQ chips, the works.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("haha i could certainly go for chips right now")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("haven't had some in years, you lucky son of a gun")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "huhu~ the only guns *i* have are fully-automatic.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("...")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "but supplies-wise, i found some bottled water")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "and... those types CDs you'd probably like i think")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Hm?")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "oh, mostly old jazz stuff")
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
    show screen phone_message_other("Kitsune", "look, i don't really know")
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
    show screen phone_message_system("&Ohms has entered #monitors.")
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
    show screen phone_message_other("Kitsune", "pls flex more, my hero~")
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
    show screen phone_message_me("goddamn.")
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
    show screen phone_message_other("Ohms", "better get your ass back in grinding hell")
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
    show screen phone_message_me("I can't believe you guys STILL play those mobile games despite the apocalypse")
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
    show screen phone_message_me("Kids today.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "omg like you're soooo old")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Look")
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
    show screen phone_message_other("Kitsune", "ok but zzzz")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "you should be playing this so we can play together")
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
    play sound "sfx/blop.mp3"
    show screen phone_message_me("ANYWAY.")
    $ renpy.pause()
    hide screen phone_sticker_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Ohms- how's the rest of the chat? You did some maintenance, right?")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "!userstats")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_system("Current users: 3. (@Stray, @Kitsune, &Ohms)")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("The most users logged in was 6. (8d ago)")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("Other users: @Realist (last login 7d ago), @Engrave (last login 12h ago), @Picoco (last login 3h ago)")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_me("jesus")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "we better check on real. let's hope he's ok.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Alright. Keep us posted.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "roger that. later o7")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_system("&Ohms has left #monitors.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "maaaaaaaan. I can't believe I forgot the event was today T_T")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("lol")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "you just don't get it. the struggle is real, ok")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("the struggle... to live?")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "the struggle to get the girl you want")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Tell me about it.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "it's certainly a good way to pass time ;3")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("I'll bet.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("I still need to finish my surveillance run though.")

    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "roger that! take care out there.")


    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "I demand a full report on my desk when you're back, soldier! o7")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("haha, copy that.")
    $ renpy.pause(0.5)
    call screen phone_reply("!logout", "notajump2")

label notajump2:

    hide screen phone_message_me
    hide phone
    hide chatphone

    play music "bgm/waiting.mp3"

    $ renpy.pause(0.5)

    
    $renpy.pause()
    "I logged out of the chat and closed the app on my phone. It looked like it was going to be another foggy day outside."
    "Not that the weather ever really changed much to begin with."
    "On the brighter side, it saved me the hassle of having to rotate my wardrobe."
    show stray normal
    with dissolve

    s "Sigh."

    nvl clear

    "I couldn't help but worry about the others. Being away for that long was more than a little concerning."
    "I quietly hoped Ohms would get back to me soon."
    "I tucked these thoughts at the back of my mind and took a granola bar from a nearby counter."

    nvl clear

    play sound "sfx/equip.mp3"
    show stray uniform
    with dissolve

    "While fastening my gloves and vest, I scanned the threadbare map hanging on the wall."
    "It depicted the quadrants of infected that needed to be constantly checked and maintained."
    "My unit happened to be placed dead center, right in the heart of the city."

    nvl clear

    hide stray
    with dissolve

        

    "The apartment I'd found myself holed up in was near the top floor of the building, overlooking the aftermath of five years ago."
    "2011 was when all of this apocalypse stuff really began. And the same chaos that you'd expect out of a zombie movie did unfold."
    "Mass panic, deaths, power and water outages... the works. I was in the military as a sniper at the time, and was stationed here after most of the containment had taken place."

    nvl clear
    
    scene bg zombies
    with fade
    $ double_vision_on("zombies")

    "But unlike the movies, these weren't just your run-of-the-mill infected corpses. They seemed like almost superior mutations."
    "We call them 'Omens'. Omens of what exactly, who knows. Laugh at the name if you want, but it's the one that stuck. It's what we've been calling them all this time."
    
    nvl clear

    "As far as we can tell, there are three categories:"
    "Good Omens,"
    "Bad Omens,"
    "and 'Grave' Omens."

    nvl clear

    "Just like your typical undead virus, the Omen infection seemed to spread through bite marks."
    "What happened after a bite, though, you didn't just die and turn into a walking corpse."
    "What {i}actually{/i} happened was much more horrific."

    nvl clear

    "After contracting the infection, the victim would catch a fever. And after the fever, a coma."
    "Parts of the face would slowly melt, only to form elsewhere on the body."
    "The Omens became just ash- or bone-pale corpses with no face, completely unrecognizable."
    "I never quite figured out where the eyes went, but the mouth always followed a sort of pattern."

    nvl clear

    "The vast majority of Omens were regular 'Bad Omens'."
    "Usually, the mouth would either remain on the face, or reform closer to the chest or stomach. They'd usually stretch to form something alien-like."
    "When you're attacked, you could see the almost-invisible creases slowly opening up for a bite."
    "To kill them, you'd have to shoot them in the head. I've also found a shot right through the mouth to be quite effective."

    nvl clear

    "On rare occasions, I'd run into a type of Omen that didn't really try to attack."
    "These ones - classified as 'Good Omens' - usually ignored people for seemingly more interesting things."
    "Scientists are still unsure as to why, but in the absence of a cure, perhaps these Omens were still clinging onto what little humanity they had left, making them more docile than most."
    "For these types, the mouth remained the same size as a regular human's, but reformed in various strange places."
    "I've seen them on hands, or arms, but I'm pretty sure they can reform on other parts of the body. I must admit I am a little curious."

    nvl clear

    "Lastly, we have 'Grave Omens.'"
    "These ones... are smarter than the rest. Almost calculating, even."
    "While Bad Omens tended to herd and wander around in different directions with no specific aim, Grave Omens seemed sentient enough to navigate and maneuver around buildings, like a trained predator."
    "I shudder to remember some of my encounters with more than a few of them. Taking them out took careful planning. They weren't nearly as predictable as their counterparts, and were much more dangerous for it."

    nvl clear

    scene bg zombiesblood
    $ double_vision_on("zombiesblood")

    "I saw one killing a comrade of mine. It moved with inhuman speed, contorting its body as it darted out, biting clean through the soldier's chest."
    "The Omen's mouth was located on its stomach, lips pursed into a smile with shark-like incisors. It relished the taste of flesh as it smeared the blood onto its featureless face, trying to remember which orifice to eat from."
    "Then it turned to me, and contemplated whether or not it should kill me, too."
    # play a gunshot?

    nvl clear

    play sound "sfx/gunshot.mp3"

    "Panicking, I shot at its head and missed, barely grazing its face."
    "The Omen formed a frown with its giant mouth, mid-chew, and ran off, never to be seen again."
    "I still wonder if that Grave Omen still roams about the city, lurking in the shadows, just waiting to finish what it started."
    "Needless to say, I try not to dwell too much on this."

    nvl clear

    "Since then, I've faced off with two other Grave Omens, neither of which I'd like to remember."
    "It's just comforting to know that I'm still here, breathing. And honing my reflexes for the next day."

    scene bg computerroom
    $ double_vision_on("computerroom")

    show stray uniform
    with dissolve

    $ renpy.pause(0.5)

    show lockphone at left
    with dissolve

    "I sighed again, looking at the screen of my locked phone. Who knows if I'll even live to see the next day?"

    hide lockphone

    play sound "sfx/equip.mp3"

    "After double-checking my equipment, I made a firm pat of my packs and grabbed my sniper rifle. I headed toward the roof to scope out the perimeter."

    nvl clear

    show bg rooftop
    with fade

    $ double_vision_on("rooftop")

    "Up on the roof, not a lot had changed."
    "It was just a flat expanse of concrete, with a few accommodations in a fenced-off corner."
    "My laundry hung near it, fluttering in the low breeze to the low screeching of Omens."
    "I had a crate propped up near the edge of the roof to mount my rifle on top. I did so, and proceeded to scope the area."

    nvl clear

    "Like yesterday, masses of Omens littered the alleys and streets."
    "I never thought I'd ever miss the loud honks and noises of the city."
    "Now it just seemed like a lingering memory as I swept my eyes across the vast, human-less landscape."

    nvl clear 
    play sound "sfx/vibrate.mp3"

    "I jolted as I felt a buzz in my pocket."

    show chatphone at left
    with dissolve

    s "Ah..."



    "I looked down at my phone, annoyed, after realizing that I didn't properly exit the chatroom app."

    stop music fadeout 1.0
    "Kitsune had logged back on to message me. It looked like she opened up a private chat window."



    play music "bgm/thumps.mp3"

    nvl clear

    
    $ renpy.pause(0.5)
    show phone at phone_pickup
    with dissolve
    $ renpy.pause()
    play sound "sfx/blop.mp3"
    show screen phone_message_system("You have joined the private chat with @Kitsune as @Stray.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_me("What's up? Kind of busy.")
    $renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Sorry, it's just")
    $renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "I was looking at the monitors")
    $renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "I couldn't help but notice an unusual amount of Omens in the west wing you were about to check out.")
    $renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Hmm. It's a little strange to hear you speaking seriously for once.")
    $renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Can it :/")
    $renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "you know I worry.")
    $renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Yeah yeah.")
    $renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Thanks for the heads up")
    $renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Any more reports before I close the app for good?")
    $renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("You know sudden alerts make me uneasy.")
    $renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Hmm... no")
    $renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Just, be careful ok? >_>")
    $renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Will do. I'll check in when I'm done.")
    $renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Mmkay. Watch your back out there.")
    $renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("I always do.")
    $ renpy.pause(0.5)
    call screen phone_reply("!logout", "kitprivatechat1")

label kitprivatechat1:
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_system("You have logged out.")
    $ renpy.pause()
    hide screen phone_message_system
    hide phone
    with dissolve

    $renpy.pause(0.5)

    hide chatphone
    show lockphone at left
    "This time, I made sure to turn off my phone and set it in my pocket."
    hide lockphone
    "I was glad Kitsune was worried, but any more sudden buzzes and I was going to lose my shit on this roof."
    "It {i}was{/i} sweet knowing that she seemed genuinely concerned, though."

    stop music fadeout 2.0
    "I stared through my scope and my mind began to wander, back to the past."


    play music "bgm/Catwn_theme.mp3"

    show bg moment
    with fade

    nvl clear

    "Kitsune and I... go a ways back. Back to when the apocalypse began."
    "We were both military, stationed in the same unit."
    "Me, a would-be sniper, training to take out and monitor Omens in densely-populated areas..."
    "And Kitsune, as tech support. She was supposedly some kind of ex-hacker, who looked to have never slept a day in her life."

    nvl clear

    "We couldn't have been bigger opposites if we tried. I literally knew nothing about technology, beyond combat and daily necessities."
    "Yet here was a girl who lived and breathed it."
    "When I ran into her for the first time, she eyed me warily and sort of paused to acknowledge my presence... only to slink off back to where she came."
    "I bristled at the greeting. While I'm usually stoic, I tend to be pretty upfront with conversation."

    nvl clear

    "Sometimes, I'd see her around base, sneaking around like she didn't belong."
    "Just kind of ambling and shuffling around muscular groups of soldiers, all of whom walked with purpose in their stride."
    "It was a bit comical, really. I started softening up around her. I'd catch myself looking for her awkward scuttle during my daily shifts before target practice."

    nvl clear

    "We'd eventually meet up for a mission in the combat room. She sort of stuttered a greeting of familiarity, giving me sideways looks as she blushed."
    "I couldn't help but let out a chuckle at how ridiculous this seemed. To my surprise, she noticed, and started to glare daggers at me... only to quickly look away."
    "I rolled my eyes, wondering if all of tech support were such nervous train wrecks."
    "But at the same time, I sort of enjoyed how refreshing her personality was, compared to the monotonous soldier lifestyle."

    nvl clear

    "One day, I noticed that my phone had stopped working."
    "Scratching my head in confusion, I spied Kitsune sneaking a bagel, and decided to enlist her for help."
    "I tapped her on the shoulder. She must have shot up at least three feet off the ground with a guilty look on her face, bagel still dangling from her mouth. Everyone in the room sort of paused at the ruckus, only to go back to talking shortly after."
    "I had the biggest shit-eating grin on my face as she gave me this exasperated huff, face flushed red with embarrassment."

    nvl clear

    "I started apologizing. I hadn't smiled that much in months."
    "I eventually brought her attention to my problem, showing her my dead phone."
    "She quickly snatched it away, and gave it a once-over. After tapping numerous places, my phone suddenly hummed back to life."
    play sound "sfx/vibrate.mp3"
    "Shoving the phone back into my hands, she quickly turned the corner and moved faster down the hall than I thought she'd ever be capable of."

    nvl clear

    "From that day on, I began pestering her, cornering her in the mess hall or break room to ask her about my phone."
    "I'm not entirely sure what possessed me to do this."
    "Why was I so interested in a scrawny nerd who didn't give me the time of day? Her world was nevertheless so fascinating."
    "Eventually, she began to understand that I was interested in learning more about technology. To my relief, she stopped running off at the sight of me."
    "Thus, we slowly began to cultivate a sort of friendship."

    stop music fadeout 1.0

    jump flashbackend

label flashbackend:
    show bg rooftopblur
    with fade

    show stray uniform
    with dissolve

    nvl clear

    play music "bgm/main stay.mp3"

    "I blinked suddenly, focusing back to reality."

    nvl clear

    show bg rooftop
    with dissolve

    $ double_vision_on("rooftop")

    "My mind wanders on the job, sometimes."
    "When it does, it always seems to settle on that part of my past."
    "I shook my head, as if shaking off bits of rain, and went back to the task at hand."

    nvl clear

    hide stray

    show bg snipe
    with fade

    "Looking through my scope, I decided to heed Kitsune's warning and do some surveillance before even attempting to thin the Omen herd."
    "I could accidentally end up getting a Grave Omen's attention, dragging it out of its territory if I wasn't careful."
    "If it noticed me, that would be bad- I haven't had a location this secure in a long while, and I'd just started getting comfortable."

    nvl clear

    "Through the glass, I checked out the cluster of Omens that seemed to be forming around one specific point."
    "I looked closer, my eyes widening in horror as I quickly ducked behind my perch."

    s "Shit. Shit shit shit."

    nvl clear

    show bg zombies
    with fade

    $ double_vision_on("zombies")

    "I started gasping, trying to slow my breathing."
    "I'd seen a group of bodies that the Omens were gathering around. Some survivors probably thought they could make a break for a clearing."

    s "{i}Damn, I'll have to fire a warning shot nearby to draw their attention.{/i}"

    "If this kept up, a horde would soon form, and I wasn't at all equipped for those types of numbers."

    nvl clear

    s "{i}And here I was hoping for a quiet day...{/i}"

    "I sighed heavily."

    nvl clear

    show bg snipe
    with dissolve

    "Steadying my breath, I went back to my perch. I lowered my face mask so I wouldn't fog up the scope."
    s "{i}Deep, even breaths.{/i}"
    s "{i}Target something safe.{/i}"
    "Looking around, I saw a dumpster where an Omen seemed to have impaled itself on one of the sharper corners."
    "If I could just angle the shot, I could wound it to draw attention away from the cluster. I looked around for other options, but this seemed like the best one."
    "I needed to act fast. Their numbers were growing."

    nvl clear

    s "{i}Alright, I'll take it.{/i}"
    "I grabbed my noise-canceling gear and stuck my earphones underneath."



    stop music fadeout 2.0

    "Turning my phone on, I plugged them in, and queued up my favorite jazz playlist to relax."
    play music "bgm/Misty.mp3"

    nvl clear

    "I could feel a familiar tune, 'Misty', wash over me, as I started to go rigid with adrenaline."

    show bg zombies
    with dissolve

    "With a practiced motion, I focused on the target, breathed evenly... and made the shot."

    play sound "sfx/gunshot.mp3"

    $renpy.pause(1.0)

    nvl clear

    show bg zombiesblood
    with dissolve

    $ double_vision_on("zombiesblood")

    "I could imagine the thunderous sound, ripping through the air, as every Omen was looking in my general direction unable to process its source."
    "I felt the recoil reverberate through my body as I stared through the scope, seeing my shot pierce through the arm of my target."


    "I saw its misplaced mouth open wide with pain, shrieking at the high-velocity impact."
    "The Omen horde noticed the commotion and began to slowly disperse, probably wary of imminent danger."

    nvl clear

    stop music fadeout 1.0


    show bg rooftop
    with fade

    $ double_vision_on("rooftop")

    show stray uniform

    "I let out a breath I didn't know I was holding, and slumped back, acknowledging my success."
    "Whenever I started shooting, be it for practice or for kills, I always set up a playlist to accompany my shots. Jazz always seemed like the genre of choice."
    "My superiors often laughed at me, warning that I'd need to be fully aware of my surroundings in the field."
    "Little did they know how wrong they were when I made every shot they threw at me. Gawking, they took back their words and shuffled away, likely to go harass some other unfortunate soldier."

    play music "bgm/main stay.mp3"

    nvl clear

    "I poked back up to survey my handiwork one last time before heading back."
    "The Omen I'd just shot at was screeching considerably less, and the others were no longer massing."
    "I didn't look forward to examining those human remains once the coast was clear, but... it had to be done sooner or later."

    nvl clear

    "I'm thinking... later."

    nvl clear

    jump chatlog2

label chatlog2:
    show bg computerroom
    with fade

    $ double_vision_on("computerroom")

    show chatphone

    "I grabbed my gear and headed back down to my room."
    "Munching on my granola bar as I walked, I started up the chat app on my phone."

    show phone at phone_pickup
    with dissolve
    $ renpy.pause()
    play sound "sfx/blop.mp3"
    show screen phone_message_system("#monitors: survivors chatroom. find the snacks and cherish them")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("Current Topic: Welcome to the end of the world!")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_system("You have now joined #monitors as @Stray.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "...and speak of the devil.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("I'll take that as a compliment.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "We know you do.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Hey hey~")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "Business as usual?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("sigh")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("you could say that")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Kit was right- there was some trouble out West. A horde was forming around some ripe ones.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "Gross :///")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "glad you're OK.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "Gotta keep an eye out.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("I always do~")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_me("In other news... got any info for me, Ohms?")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "Hm? Oh right")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "I was getting an update on the others.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "Still haven't heard from Realist. I'm getting a bit worried... but I'll keep you all updated.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "Picoco is fine. She's just busy with clearing out some new wards, but otherwise A-OK.")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "And Engrave said they'd be on later tonight...")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_system("@Engrave has entered #monitors.")
    $ renpy.pause()
    hide screen phone_message_system
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "or... now?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("Yo.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "o7")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", "yo")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Eng", "Hey hey")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Eng", "y'all miss me?")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me("It's only been 12 hours.")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Eng", "Enough time to see me dead and wanderin ;3~")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_me(">_>")
    $ renpy.pause()
    hide screen phone_message_me
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Ohms", ">_>")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Kitsune", "¯\_(-_-)_/¯  ")
    $ renpy.pause()
    hide screen phone_message_other
    play sound "sfx/blop.mp3"
    show screen phone_message_other("Eng", "¯\_(-_-)_/¯  ")
    $ renpy.pause()

    nvl clear 



##Hide cellphone screen

    
    
label continues:
    return 