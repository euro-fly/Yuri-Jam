# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    image computerroom = Image("images/bg/ComputerRoom.png")
    image rooftop = Image("images/bg/Rooftop.png")
    image zombies = Image("images/scenes/zombies_default.png")
    image zombiesblood = Image("images/scenes/zombies_blood.png")
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

    hide screen phone_message_meR
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
    with fade
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

    play music "bgm/main stay.mp3"

    hide chatphone
    show lockphone at left
    "This time, I made sure to turn off my phone and set it in my pocket."
    hide lockphone
    "I was glad Kitsune was worried, but any more sudden buzzes and I was going to lose my shit on this roof."
    "It {i}was{/i} sweet knowing that she seemed genuinely concerned, though."
    "I stared through my scope and my mind began to wander, back to the past."

##Hide cellphone screen

    
    
label continues:
    return 