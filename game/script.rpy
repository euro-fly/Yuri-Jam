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

image bg wasteland = "images/wasteland.jpg"
image bg wip = "images/bg/bg wip.png"
image bg computerroom = "images/bg/ComputerRoom.png"
image bg computerblur = "images/bg/ComputerRoom-blur.png"
image bg rooftop = "images/bg/Rooftop.png"
image bg rooftopblur = "images/bg/Rooftop-blur.png"

image bg black = "#000"

image stray normal = "images/sprites/stra-default.png"
image stray upset = "images/sprites/stra-upset.png"
image stray embarrassed = "images/sprites/stra-emba.png"
image stray frown = "images/sprites/stra-frown.png"
image stray talk = "images/sprites/stra-open-default.png"
image stray blush = "images/sprites/stra-smileblsh.png"
image stray smile = "images/sprites/stra-smilepng.png"
image stray uniform = "images/sprites/stra-uniform.png"

image kitsune normal = "images/sprites/kitsune-phone.png"
image kitsune baited = "images/sprites/kit_baited_phone.png"
image kitsune smile = "images/sprites/kit_smile_phone.png"
image kitsune smug = "images/sprites/kit_smug_phone.png"
image kitsune talk = "images/sprites/kit_talk_phone.png"
image kitsune angry = "images/sprites/kit_angry_phone.png"

image smartphone chat = "images/phone/phone-def.png"
image smartphone lock = "images/phone/phone-default.png"
image smartphone calling = "images/phone/phone-no glove.png"

image bg zombies = "images/scenes/zombies_default.png"
image bg zombiesblood = "images/scenes/zombies_blood.png"
image bg moment = "images/scenes/moment.png"
image bg snipe = "images/scenes/snipe.png"
image bg together = "images/scenes/together.png"
image bg credits = "images/scenes/credits-rooftop.png"



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
    easeout 0.1 yoffset -20 alpha 0
        
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
    call hide_all() from _call_hide_all
    $ renpy.pause(0.1)
    play sound "sfx/blop.mp3"
    if who.lower() == "stray":
        show screen phone_message_me(what)
    elif who.lower() == "system":
        show screen phone_message_system(what)
    elif who != "":
        show screen phone_message_other(who, what)
    return

label sticker(who, what):
    $ renpy.pause()
    call hide_all() from _call_hide_all_1
    $ renpy.pause(0.1)
    play sound "sfx/blop.mp3"
    if who.lower() == "stray":
        show screen phone_sticker_me(what)
    elif who != "":
        show screen phone_sticker_other(who, what)
    return

label hide_all():
    hide screen phone_message_other
    hide screen phone_message_me
    hide screen phone_message_system
    hide screen phone_sticker_other
    hide screen phone_sticker_me
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

    show smartphone chat at left
    with dissolve 
    ## Add cellphone screen here
    $ renpy.pause(0.5)

    show phone at phone_pickup
    with dissolve

    call message("system", "#monitors: survivors chatroom for general bullshit") from _call_message
    call message("system", "Current Topic: Welcome to the end of the world!") from _call_message_1
    call message("system", "You have now joined #monitors as @Stray.") from _call_message_2
    call message("system", "@Kitsune has entered #monitors.") from _call_message_3
    call message("Stray", "Hey") from _call_message_4
    call message("Stray", "How's it going?") from _call_message_5
    call message("Kitsune", "Hey hey~") from _call_message_6
    call message("Kitsune", "Just got up.") from _call_message_7
    call message("Stray", "Same") from _call_message_8
    call message("Stray", "Let's see how fucked we are today.") from _call_message_9

    $ renpy.pause(0.5)
    call screen phone_reply("!todaystatus", "notajump")
    
label notajump:

    hide screen phone_message_me
    $ renpy.pause(0.5)

    call message("system", "Current temperature: 61F/16C. Cloudy with possible showers.") from _call_message_10
    call message("system", "Headline #6661: Year Five of the ongoing Omen crisis. Situation still grave, as usual. No progress on a cure.") from _call_message_11
    call message("system", "Attack reported in California at 1300 hours, with 10 dead.") from _call_message_12
    call message("system", "Refer to !pop for current population data.") from _call_message_13
    call message("Kitsune", "Looking grim~") from _call_message_14
    call message("Stray", "tell me something I don't know.") from _call_message_15
    call message("Kitsune", "wow, someone's full of sunshine today.") from _call_message_16
    call message("Kitsune", "feeling lonely?") from _call_message_17
    call message("Stray", "oh shut up.") from _call_message_18
    call message("Kitsune", "hmm") from _call_message_19
    call message("Kitsune", "well if it makes you feel any better") from _call_message_20
    call message("Kitsune", "I mapped out some of the uncharted waters around my place") from _call_message_21
    call message("Kitsune", "found an empty home") from _call_message_22
    call message("Kitsune", "WITH UNTOUCHED SNACKS") from _call_message_23
    call message("Stray", "AAAAAAA") from _call_message_24
    call message("Kitsune", "yep!!") from _call_message_25
    call sticker("Kitsune", "chips") from _call_sticker
    call message("Kitsune", "just to make you jealous.") from _call_message_26
    call message("Kitsune", "i had no idea salty chips could ever taste so sweet.") from _call_message_27
    call message("Kitsune", "found a can of pringles, but i've also got funyuns, BBQ chips, the works.") from _call_message_28
    call message("Stray", "haha i could certainly go for chips right now") from _call_message_29
    call message("Stray", "haven't had some in years, you lucky son of a gun") from _call_message_30
    call message("Kitsune", "huhu~ the only guns *i* have are fully-automatic.") from _call_message_31
    call message("Stray", "...") from _call_message_32
    call message("Kitsune", "but supplies-wise, i found some bottled water") from _call_message_33
    call message("Kitsune", "and... those types CDs you'd probably like i think") from _call_message_34
    call message("Stray", "Hm?") from _call_message_35
    call message("Kitsune", "oh, mostly old jazz stuff") from _call_message_36
    call sticker("Kitsune", "jazz") from _call_sticker_1
    call message("Kitsune", "like, we've got... one of em was by Miles something or other.") from _call_message_37
    call message("Kitsune", "then you had the... cannon ball?") from _call_message_38
    call message("Kitsune", "look, i don't really know") from _call_message_39
    call message("Kitsune", "it seemed like it was your kinda thing is all") from _call_message_40
    call message("Stray", "Yeah yeah.") from _call_message_41
    call message("Kitsune", "How are things on your end?") from _call_message_42
    call message("Stray", "Hmm") from _call_message_43
    call message("Stray", "Went up top today to do a surveillance sweep, all clear so far.") from _call_message_44
    call message("Stray", "Weather is *still* foggy as shit.") from _call_message_45
    call message("Stray", "Omens are gathering in the usual spots, so I picked a number of them off today.") from _call_message_46
    call message("Kitsune", "My hard little worker~") from _call_message_47
    call message("Stray", ">_>") from _call_message_48
    call message("system", "&Ohms has entered #monitors.") from _call_message_49
    call message("Kitsune", "Oh hey Ohms! o/") from _call_message_50
    call message("Stray", "yo") from _call_message_51
    call message("Ohms", "You kids. Flirting while I'm not around.") from _call_message_52
    call message("Stray", "uuuuuugh") from _call_message_53
    call message("Kitsune", "hahahahaha") from _call_message_54
    call message("Ohms", "Anyways") from _call_message_55
    call message("Ohms", "how goes it?") from _call_message_56
    call message("Kitsune", "Oh, Stray here was just telling me of her heroic tales") from _call_message_57
    call message("Kitsune", "Killing Omens left and right on surveillance duty") from _call_message_58
    call message("Kitsune", "pls flex more, my hero~") from _call_message_59
    call message("Stray", "Save me.") from _call_message_60
    call message("Ohms", "lol. your problem not mine.") from _call_message_61
    call message("Stray", "...") from _call_message_62
    call message("Stray", "how have you been, ohms?") from _call_message_63
    call message("Ohms", "eh, same old same old") from _call_message_64
    call message("Ohms", "stayed holed-up. played some net games.") from _call_message_65
    call message("Ohms", "just shut-in things.") from _call_message_66
    call message("Ohms", "I should prob go out and stretch my legs, do some killing.") from _call_message_67
    call message("Ohms", "But. You know how it is where I am.") from _call_message_68
    call message("Stray", "mm.") from _call_message_69
    call message("Ohms", "er") from _call_message_70
    call message("Ohms", "doing okay there, stray?") from _call_message_71
    call message("Stray", "oh") from _call_message_72
    call message("Stray", "my bad. kit was just showing off her snack haul.") from _call_message_73
    call message("Stray", "goddamn.") from _call_message_74
    call message("Ohms", "oh what") from _call_message_75
    call message("Ohms", "lmao I see it") from _call_message_76
    call message("Ohms", "daaaaaamn. funyuns, too?") from _call_message_77
    call message("Kitsune", "damn straight!") from _call_message_78
    call message("Ohms", "eyyyyy") from _call_message_79
    call message("Stray", "...") from _call_message_80
    call message("Stray", "I hope they're SOGGY AS SHIT.") from _call_message_81
    call message("Kitsune", "wow rude") from _call_message_82
    call message("Ohms", "^") from _call_message_83
    call message("Ohms", "but that aside. how goes surveillance, Stray? going out again today?") from _call_message_84
    call message("Stray", "yeah. most likely.") from _call_message_85
    call message("Stray", "the west wing still needs to be secured.") from _call_message_86
    call message("Ohms", "sounds rough.") from _call_message_87
    call message("Stray", "eh. it is what it is.") from _call_message_88
    call message("Kitsune", "not just strong, but humble too~ what a hero.") from _call_message_89
    call message("Stray", ">________>") from _call_message_90
    call message("Ohms", "ah, yes. this is what i am here for.") from _call_message_91
    call message("Stray", "Ugh not you too?") from _call_message_92
    call message("Ohms", "hey, look man") from _call_message_93
    call message("Ohms", "it's not like I have anything better to do") from _call_message_94
    call message("Ohms", "Kitsune- oh btw") from _call_message_95
    call message("Kitsune", "what's up?") from _call_message_96
    call message("Ohms", "event's up. how far have you gotten?") from _call_message_97
    call message("Kitsune", "OH") from _call_message_98
    call message("Kitsune", "Shit, that's TODAY?") from _call_message_99
    call message("Ohms", "yep.") from _call_message_100
    call message("Ohms", "better get your ass back in grinding hell") from _call_message_101
    call message("Kitsune", "FFFFFFFFFfffffff") from _call_message_102
    call message("Kitsune", "fffffff") from _call_message_103
    call message("Kitsune", "fff") from _call_message_104
    call message("Stray", "Yeah no") from _call_message_105
    call message("Stray", "I can't believe you guys STILL play those mobile games despite the apocalypse") from _call_message_106
    call message("Kitsune", "IT'S WHAT I LIVE FOR.") from _call_message_107
    call message("Ohms", "SAME.") from _call_message_108
    call message("Stray", "Kids today.") from _call_message_109
    call message("Kitsune", "omg like you're soooo old") from _call_message_110
    call message("Stray", "Look") from _call_message_111
    call sticker("stray","ps2") from _call_sticker_2
    call message("Stray", "There's a working PS2 and a backlog to last you DAYS") from _call_message_112
    call message("Kitsune", "ok but zzzz") from _call_message_113
    call message("Kitsune", "you should be playing this so we can play together") from _call_message_114
    call message("Stray", "Pass.") from _call_message_115
    call message("Kitsune", ":'(") from _call_message_116
    call message("Ohms", "rip") from _call_message_117
    call message("Stray", "ANYWAY.") from _call_message_118
    call message("Stray", "Ohms- how's the rest of the chat? You did some maintenance, right?") from _call_message_119
    call message("Ohms", "Oh yeah, lemme check") from _call_message_120
    call message("Ohms", "!userstats") from _call_message_121
    call message("system", "Current users: 3. (@Stray, @Kitsune, &Ohms)") from _call_message_122
    call message("system", "The most users logged in was 6. (8d ago)") from _call_message_123
    call message("system", "Other users: @Realist (last login 7d ago), @Engrave (last login 12h ago), @Picoco (last login 3h ago)") from _call_message_124
    call message("Stray", "jesus") from _call_message_125
    call message("Ohms", "we better check on real. let's hope he's ok.") from _call_message_126
    call message("Stray", "Alright. Keep us posted.") from _call_message_127
    call message("Ohms", "roger that. later o7") from _call_message_128
    call message("system", "&Ohms has left #monitors.") from _call_message_129
    call message("Kitsune", "maaaaaaaan. I can't believe I forgot the event was today T_T") from _call_message_130
    call message("Stray", "lol") from _call_message_131
    call message("Kitsune", "you just don't get it. the struggle is real, ok") from _call_message_132
    call message("Stray", "the struggle... to live?") from _call_message_133
    call message("Kitsune", "the struggle to get the girl you want") from _call_message_134
    call message("Stray", "Tell me about it.") from _call_message_135
    call message("Kitsune", "it's certainly a good way to pass time ;3") from _call_message_136
    call message("Stray", "I'll bet.") from _call_message_137
    call message("Stray", "I still need to finish my surveillance run though.") from _call_message_138
    call message("Kitsune", "roger that! take care out there.") from _call_message_139
    call message("Kitsune", "I demand a full report on my desk when you're back, soldier! o7") from _call_message_140
    call message("Stray", "haha, copy that.") from _call_message_141

    $ renpy.pause(0.5)
    call screen phone_reply("!logout", "notajump2")

label notajump2:

    hide screen phone_message_me
    hide phone
    hide smartphone chat

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

    show smartphone lock at left
    with dissolve

    "I sighed again, looking at the screen of my locked phone. Who knows if I'll even live to see the next day?"

    hide smartphone lock

    play sound "sfx/equip.mp3"

    "After double-checking my equipment, I made a firm pat of my packs and grabbed my sniper rifle. I headed toward the roof to scope out the perimeter."

    nvl clear

    show bg rooftop
    with Fade(0.5,1.0,0.5)

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

    show smartphone chat at left
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

    call message("system", "You have joined the private chat with @Kitsune as @Stray.") from _call_message_142


    call message("Stray", "What's up? Kind of busy.") from _call_message_143
    call message("Kitsune", "Sorry, it's just") from _call_message_144

    call message("Kitsune", "I was looking at the monitors") from _call_message_145

    call message("Kitsune", "I couldn't help but notice an unusual amount of Omens in the west wing you were about to check out.") from _call_message_146
    call message("Stray", "Hmm. It's a little strange to hear you speaking seriously for once.") from _call_message_147

    call message("Kitsune", "Can it :/") from _call_message_148

    call message("Kitsune", "you know I worry.") from _call_message_149

    call message("Stray", "Yeah yeah.") from _call_message_150
    call message("Stray", "Thanks for the heads up") from _call_message_151
    call message("Stray", "Any more reports before I close the app for good?") from _call_message_152
    call message("Stray", "You know sudden alerts make me uneasy.") from _call_message_153
    call message("Kitsune", "Hmm... no") from _call_message_154

    call message("Kitsune", "Just, be careful ok? >_>") from _call_message_155
    call message("Stray", "Will do. I'll check in when I'm done.") from _call_message_156

    call message("Kitsune", "Mmkay. Watch your back out there.") from _call_message_157
    call message("Stray", "I always do.") from _call_message_158

    $ renpy.pause(0.5)
    call screen phone_reply("!logout", "kitprivatechat1")

label kitprivatechat1:
    call message("system", "You have logged out.") from _call_message_159
    $ renpy.pause()
    $ renpy.pause(0.1)
    hide screen phone_message_system

    hide phone
    with dissolve

    $renpy.pause(0.5)

    hide smartphone chat
    show smartphone lock at left
    "This time, I made sure to turn off my phone and set it in my pocket."
    hide smartphone lock
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
    play music "bgm/Misty_pi.mp3"

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
    with Fade(0.5, 1.0, 0.5)

    $ double_vision_on("computerroom")

    show smartphone chat at left
    with dissolve

    "I grabbed my gear and headed back down to my room."
    "Munching on my granola bar as I walked, I started up the chat app on my phone."

    show phone at phone_pickup
    with dissolve

    call message("system", "#monitors: survivors chatroom. find the snacks and cherish them") from _call_message_160
    call message("system", "Current Topic: Welcome to the end of the world!") from _call_message_161
    call message("system", "You have now joined #monitors as @Stray.") from _call_message_162
    call message("Ohms", "...and speak of the devil.") from _call_message_163
    call message("Stray", "I'll take that as a compliment.") from _call_message_164
    call message("Ohms", "We know you do.") from _call_message_165
    call message("Kitsune", "Hey hey~") from _call_message_166
    call message("Ohms", "Business as usual?") from _call_message_167
    call message("Stray", "sigh") from _call_message_168
    call message("Stray", "you could say that") from _call_message_169
    call message("Stray", "Kit was right- there was some trouble out West. A horde was forming around some ripe ones.") from _call_message_170
    call message("Kitsune", "Gross :///") from _call_message_171
    call message("Kitsune", "glad you're OK.") from _call_message_172
    call message("Ohms", "Gotta keep an eye out.") from _call_message_173
    call message("Stray", "I always do~") from _call_message_174
    call message("Stray", "In other news... got any info for me, Ohms?") from _call_message_175
    call message("Ohms", "Hm? Oh right") from _call_message_176
    call message("Ohms", "the status update on the others.") from _call_message_177
    call message("Ohms", "Still haven't heard from Realist. I'm getting a bit worried... but I'll keep you all updated.") from _call_message_178
    call message("Ohms", "Picoco is fine. She's just busy with clearing out some new wards, but otherwise A-OK.") from _call_message_179
    call message("Ohms", "And Engrave said they'd be on later tonight...") from _call_message_180
    call message("system", "@Engrave has entered #monitors.") from _call_message_181
    call message("Ohms", "or... now?") from _call_message_182
    call message("Stray", "Yo.") from _call_message_183
    call message("Kitsune", "o7") from _call_message_184
    call message("Ohms", "yo") from _call_message_185
    call message("Eng", "Hey hey") from _call_message_186
    call message("Eng", "y'all miss me?") from _call_message_187
    call message("Stray", "It's only been 12 hours.") from _call_message_188
    call message("Eng", "Enough time to see me dead and wanderin ;3~") from _call_message_189
    call message("Stray", ">_>") from _call_message_190
    call message("Ohms", ">_>") from _call_message_191
    call message("Kitsune", "¯\_(-_-)_/¯  ") from _call_message_192
    call message("Eng", "¯\_(-_-)_/¯  ") from _call_message_193
    call message("Eng", "Seriously though, my bad") from _call_message_194
    call message("Eng", "I had to thin out the Omens near my city's entrance") from _call_message_195
    call message("Eng", "What a major pain that was") from _call_message_196
    call message("Eng", "Really shoulda checked in sooner") from _call_message_197
    call message("Stray", "You alright?") from _call_message_198
    call message("Eng", "Heh, yeah") from _call_message_199
    call message("Eng", "It's just not something I want to deal with on the reg") from _call_message_200
    call message("Stray", "Yeah, I'm concerned that hordes are forming more frequently it seems") from _call_message_201
    call message("Stray", "We'll def have to keep a bigger eye out for more survivors") from _call_message_202
    call message("Stray", "Most of em don't know how to maneuver about the cities, so we should try to get to them first") from _call_message_203
    call message("Ohms", "Agreed") from _call_message_204
    call message("Ohms", "Kit, could you set up a frequency that's easy to access?") from _call_message_205
    call message("Ohms", "Easier to give out information that way, if they happen to wander into the cities") from _call_message_206
    call message("Kitsune", "On it") from _call_message_207
    call message("Kitsune", "I'll send out the frequency info when it's up.") from _call_message_208
    call message("Stray", "Actually getting work done in chat") from _call_message_209
    call message("Stray", "*slow claps*") from _call_message_210
    call message("Eng", "ikr?") from _call_message_211
    call message("Kitsune", "ugh, you guys treat me like such a child") from _call_message_212
    call message("Eng", "but you aaaaare") from _call_message_213
    call message("Eng", "Our lil baby <3") from _call_message_214
    call message("Ohms", "Baby Kit.") from _call_message_215
    call message("Stray", "I can't disagree.") from _call_message_216
    call message("Kitsune", "just so you all know") from _call_message_217
    call message("Kitsune", "I'm giving you all the bird right now") from _call_message_218
    call message("Eng", "Lil baby's first swear!") from _call_message_219
    call message("Eng", "I'm...") from _call_message_220
    call message("Eng", "I'm so proud *sheds tear*") from _call_message_221
    call message("Kitsune", ":<<<<<") from _call_message_222
    call message("Ohms", "lol") from _call_message_223
    call message("Stray", "lol") from _call_message_224
    call message("Eng", "In my defense") from _call_message_225
    call message("Eng", "can you honestly say you *aren't* grinding out the current idol event at this very instant?") from _call_message_226
    call message("Kitsune", "...no comment") from _call_message_227
    call message("Ohms", "At least *I* finished my run. I'm sleeping for days.") from _call_message_228
    call message("Stray", "Well I mean") from _call_message_229
    call message("Stray", "As long as she can multitask") from _call_message_230
    call message("Stray", "I won't complain") from _call_message_231
    call message("Stray", "At least she hasn't somersaulted into the toilet, yet.") from _call_message_232
    call message("Stray", "I still can't believe how you even managed it, Engrave.") from _call_message_233
    call message("Eng", "Look, man, it made for a good story at the time.") from _call_message_234
    call message("Stray", "I see we're setting only the highest standards.") from _call_message_235
    call message("Kitsune", "lolololol") from _call_message_236
    call message("Eng", "Don't I always~?") from _call_message_237
    call message("Eng", "Anyway, I'm out") from _call_message_238
    call message("Eng", "Back to work, peace o7") from _call_message_239
    call message("Stray", "o7") from _call_message_240
    call message("Kitsune", "o7") from _call_message_241
    call message("Ohms", "o7") from _call_message_242
    call message("System", "@Engrave has signed out of #monitors.") from _call_message_243
    call message("Ohms", "I'm out, too") from _call_message_244
    call message("Ohms", "gotta get some sleep!") from _call_message_245
    call message("Ohms", "cya o/") from _call_message_246
    call message("Stray", "Later o/") from _call_message_247
    call message("Kitsune", "bye~") from _call_message_248
    call message("System", "&Ohms has signed out of #monitors.") from _call_message_249
    call message("Kitsune", "Hey") from _call_message_250
    call message("Kitsune", "I'mma message you") from _call_message_251
    call message("Stray", "kk") from _call_message_252
    jump flashbacktower

label flashbacktower:

    stop music fadeout 2.0
    $ renpy.pause(2.0)
    play music "bgm/waiting.mp3"

    call message("System", "You have joined the private chat with @Kitsune as @Stray.") from _call_message_253
    call message("Stray", "What's up?") from _call_message_254
    call message("Kitsune", "What were you saying about that horde earlier?") from _call_message_255
    call message("Kitsune", "Like") from _call_message_256
    call message("Kitsune", "Do you want to talk about it?") from _call_message_257
    call message("Kitsune", "It's just. I saw it on my monitor. It could have turned into a total shitstorm if you hadn't dealt with it asap.") from _call_message_258
    call message("Stray", "mm") from _call_message_259
    call message("Kitsune", "It's okay") from _call_message_260
    call message("Kitsune", "You don't have to downplay anything") from _call_message_261
    call message("Kitsune", "We all know how shitty it can get out there") from _call_message_262
    call message("Kitsune", "I... I can call you.") from _call_message_263
    call message("Kitsune", "Can I call you? So we can talk?") from _call_message_264
    call message("Stray", "hahaha") from _call_message_265
    call message("Kitsune", "w-what >>;;") from _call_message_266
    call message("Stray", "Nah it's nothing. Only teasing") from _call_message_267
    call message("Stray", "I'd... like that, though") from _call_message_268
    call message("Kitsune", "kk. gimme a few, brb.") from _call_message_269
    call message("Stray", "aight") from _call_message_270

    call hide_all() from _call_hide_all_2

    nvl clear

    hide smartphone
    hide phone

    stop music fadeout 2.0
    $ renpy.pause(2.0)
    play music "bgm/main stay.mp3"

    show stray normal
    with dissolve

    "Sometimes, after a chat with the team, or after a particularly long day, Kitsune would ask me in a private message if I was doing alright."

    show smartphone lock at left behind stray
    with dissolve

    show stray blush

    "I stared blankly at my phone, feeling my mouth form into a smile."
    "Days like this did tend to take their toll on me, as I'm sure it did on everyone."
    "It was just nice, knowing I had someone close to me, someone who knew me before all this happened."

    show stray normal

    hide smartphone
    with dissolve

    nvl clear

    "I scratched at the scar on my face absentmindedly."
    "The nerves were all damaged, so it felt like I was just touching an accessory attached to my face."
    "It was a nervous habit I developed after the accident."
    "I tended to do it when I was unsure of what to do with myself."

    nvl clear 

    "Shortly after Kitsune and I had sort-of-kind-of formed a friendship, I was sent off to help escort a cargo of rations to a nearby survivor camp."
    "It seemed simple enough: I was to hang close by at a vantage point, and make sure the cargo was free of Omens and would-be scavengers."
    "Near the turning point of the mission, things went to hell real quick. A large group of raiders surrounded the vehicle."
    "Despite my warnings... the convoy was overrun. But not before the truck hit a land mine. The explosion took the truck and the raiders both."

    nvl clear

    "I scratched again at my scar."

    nvl clear

    show stray frown

    "I was high up, on an abandoned water tower at the time."
    "All things considered, I got out lucky- it only cost me the side of my face. No one else survived."
    "My superiors realized how much of a disaster this mission turned out to be as they rushed me to the surgical unit."
    "I couldn't stop clawing at my seared face in pain."

    nvl clear

    "When Kitsune saw just how bad my wounds were, she rushed over, practically wrestling with the medical team just to stay at my side."
    "{i}Why did she care so much,{/i} I wondered, as I drifted in and out of consciousness."

    nvl clear

    "After the surgery, my face was a bandaged mess. I could still feel the warmth of Kitsune's hand in mine on the hospital bed."

    show stray blush

    "I tried my hardest not to smile."

    jump kit_call

label kit_call:


    hide stray
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    play music "bgm/thumps.mp3"
    play sound "sfx/vibrate.mp3"
    $ renpy.pause(0.5)

    show smartphone calling at left
    with dissolve

    "My phone began to vibrate with the obnoxious ringtone Kitsune had set on my phone years ago."
    "It sounded like... some god-awful anime house mash-up with a cat's screams mixed in."
    "If it ever went off, and the Omens heard it... at least I'd die of embarrassment before they could kill me."

    nvl clear
    show stray normal
    with dissolve

    show stray normal at midleft
    with move

    hide smartphone
    with dissolve

    $ renpy.pause(0.5)

    show kitsune normal at midright
    with dissolve

    k "Hey hey! Sorry about the call quality. It's probably crap."
    k "The look on your face tells me you haven't changed the work of art I set as your ringtone."

    show stray frown

    s "That's... one way of looking at it."
    k "Hmhmm~ Anyway. Tell me about what happened today."

    show stray normal

    "I gave Kitsune the gist of what had happened today, leaving out the parts where I'd lost my nerve."
    "I figured she picked up on it all the same, if her frowns were anything to go by."

    nvl clear

    k "Well... I hope you're doing better now."
    s "I am, thanks. I mean, I know I tend to be pretty stoic most of the-"

    show kitsune angry

    k "{i}All{/i} of the time."
    s "Right, but... trust me when I say I feel better, so..."

    show stray frown

    s "Sorry..."

    show kitsune smile
    "I could see her expression visibly soften at my apology."
    "I relaxed a bit. It's hard for me to be put on the spot like that... I'm just not used to the attention."
    "I scratched at my scar."

    nvl clear
    show kitsune normal
    show stray normal

    k "Ah- your scar! Does it still hurt? Have you been taking care of it?"

    show stray blush

    s "*chuckles* Yeah, yeah."

    show kitsune angry

    k "HEY, I'm serious! You should remember to use that moisturizer every day, and-"

    show stray embarrassed

    s "Thanks, Mom."
    k "*huffs*"
    s "Hey, I mean... it's not like there's all that much left on my face, anyway."
    s "Why bother, you know? Who would even find this mess attractive?"

    show kitsune smile

    k "You {i}would{/i} say that, jeez."

    show kitsune baited

    "Kitsune quickly turned her head away, embarrassed. {i}Maybe I could drag this out a bit more,{/i} I thought to myself, grinning."

    nvl clear

    show stray smile

    s "But if I knew a certain {i}someone{/i} who did... I certainly wouldn't mind hearing them say so?"
    k "Sh- shut up."

    show stray normal

    s "Haha. Anyway, how are you doing? I missed hearing your voice."

    show kitsune talk

    k "Mmmm... well enough, I guess? I've been monitoring your area, and the others'."
    k "So far so good, minus the little hiccup I mentioned to you. I agree with Ohms' decision about putting out a public radio frequency for survivors."

    show stray frown

    "I nodded gravely, wondering if that would have saved the group I'd seen earlier today."

    nvl clear
    show kitsune normal

    k "Hey, look. It's not your fault..."
    s "Mm..."

    "I blinked, fully aware that Kitsune had just read my mind."

    nvl clear

    s "I know, but..."

    show kitsune smug

    k "No buts! I'll put out that signal ASAP, okay?"

    show stray talk

    s "Yeah, okay."

    show stray smile

    stop music fadeout 2.0

    "I smiled, knowing that she'd always get fired-up when I was involved... even in spite of her normally meek personality."
    "I caught a glimpse of her grin, though and prepared myself for the worst."

    nvl clear

    play music "bgm/waiting.mp3"

    show kitsune smug

    k "You're looking good in your fatigues, though... that sort of stuff is my favorite~"

    show stray frown

    s "Ugh."

    "Fortunately, I'd already changed out of most of my gear."

    show kitsune baited

    "Kitsune was... a bit of a military otaku."
    "Even though she couldn't shoot for shit, she still knew quite a bit about the technology."

    show kitsune normal

    k "You're still using the M-40, right? Standard military-issue?"
    k "Well, I suppose that's for the best... it's the easiest to get bullets for, since we still get them dropped in from base..."

    "I frowned, knowing that she was going to burst into some long-winded explanation about a feature on my gun that I knew next to nothing about."
    "I knew how to shoot and maintain my weapons, as well as how to assess when and when not to draw. That was enough for me." 
    "It probably sounds like torture to someone who's never seriously held a gun in her life."

    nvl clear

    "I appreciated the wealth of knowledge when I actually had questions, but this was a conversation for another time."
    "I cut her off with a sharp look."

    nvl clear

    show kitsune baited

    k "A-anyway. Other than that, you know I've been just playing a bunch of net and mobile games, but I don't want to bore a dinosaur like you with the small stuff."

    show stray talk
    

    s "Hey, whoa, now. Not {i}everything{/i} I play is old-school. Don't tell me you consider Wii games retro."

    show kitsune normal

    k "..."

    show kitsune baited

    k "..."

    show stray frown

    s "{i}GOD.{/i}"

    show kitsune smile

    k "I'm joking! Had you going there, didn't I. I owned a Wii, too. Still a PS3 lifer, I'm sorry to say."

    show stray smile

    s "It {i}did{/i} have some kick-ass RPGs."
    k "I'm glad we see eye to eye."

    show kitsune normal

    k "But I remember when you had me back at base, playing those old SNES and PS2 games. Gotta say, they still hold up."

    show stray talk

    s "Just wait until you've played the classics."
    k "Look, I've got this thing called an 'emulator', and..."

    $ renpy.pause(0.5)

    show stray smile

    $ renpy.pause(0.5)
    show kitsune angry

    k "DON'T YOU SCOFF."
    s "Well, as long as you're playing them, I guess I can't {i}really{/i} complain..."

    show kitsune normal

    k "Where you find the time to go digging through abandoned game stores and basements is beyond me."

    show stray normal

    s "It passes the time. Plus, I get a kick out of continuing from old save files. It feels like I'm helping the previous owners move on..."
    s "Especially if they've saved before a boss in the worst possible spots."

    show kitsune smile

    k "I hear you. One time, I passed by an actual arcade machine. It reminded me of you."

    show stray talk

    s "Really? Did you take a picture?"
    k "Yeah... but don't ask me where I put it."

    show stray frown

    s "Figures."

    show stray talk

    k "But... hey?"

    show stray normal

    s "Hmm?"

    show kitsune baited

    k "Are you... really doing okay?"

    show stray smile

    s "Heh. I remember when you were so jumpy and nervous around me. Where does the time go?"

    show kitsune smile

    k "Hmph. Don't try to dodge the question, you know I'll keep pestering you."

    show stray talk

    s "Alright, alright. You caught me. {i}I'm okay.{/i} That better?"

    show kitsune talk

    k "Better."

    show stray normal

    s "Hey..."

    show kitsune smug

    k "Hmm?"

    show stray blush

    s "Thanks. I know I can be really difficult, but... talking through this really does make me feel a lot better."

    show kitsune baited

    "She looked away nervously, but nodded in agreement, making a small noise of affirmation."

    s "I know I'm not the most sensitive person in the world, but... I'm here for you, too. Okay?"

    k "I know... you big dummy."

    show stray smile

    s "Nice."
    s "I'm gonna get going. I have to finish up some stuff... catch you around?"

    k "Yeah."

    show kitsune smile

    k "Catch you around."

    show stray talk

    "I opened my mouth to say something more..."

    show stray smile

    "But we both paused, our smiles softening as I ended the call."

    stop music fadeout 2.0

    hide kitsune

    nvl clear

    $ renpy.pause(1.0)

    show smartphone lock

    $ renpy.pause(1.0)

    play music "bgm/main stay.mp3"

    hide smartphone

    show stray at center
    with move

    "After I hung up, I took out an old photo."
    "A close buddy of mine took a candid shot of me and Kitsune, and gave it to me as a birthday present."

    hide stray

    show bg together
    with Fade(0.5,0.5,0.5)

    nvl clear

    "I knew Kitsune would roll her eyes at how old-school I was by keeping a physical photo around. Nevertheless, I was still really attached to it."
    "It really summed up the two of us: our personalities, that is."
    "Me, looking off into the distance both surly and embarrassed, face full of bandages fresh from surgery..."
    "And Kitsune, holding onto me, in a comforting but forceful grip."

    nvl clear

    "Despite the fact that we were cities apart, we could still maintain that same connection, thanks to technology."
    "She's here for me."
    "I'm here for her."

    nvl clear

    "I smiled, placing the picture snugly back into my chest pocket."
    "I went back outside onto the rooftop. I should finish what I started."
    "Time to take on another day."

    nvl clear

    stop music fadeout 1.0
    $ renpy.pause(1.0)


    jump creditroll    
    
label creditroll:
    play music "bgm/Catwn_theme.mp3"
    show bg credits
    with Fade(0.5,1.0,0.5)

    $ renpy.pause()

    show bg black
    with Fade(0.5,1.0,0.5)

    $ renpy.pause(1.0)
    return 