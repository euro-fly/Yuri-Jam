# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define s = Character('Stray', color="#c8ffc8")

define k = Character('Kitsune', color="#c8f4ff")

image phone = "images/phone/bustedphone.png"
image bg wasteland = "images/wasteland.jpg"
image bg wip = "images/bg/bg wip.png"

image eileen normal = "images/sylvie_normal.png"
image eileen giggle = "images/sylvie_giggle.png"
image eileen smile = "images/sylvie_smile.png"
image eileen surprised = "images/sylvie_surprised.png"

image stray normal = "images/sprites/Stray - Neutral.png"

image kitsune giggle = "images/sprites/phone.gif"



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
    
    play music "bgm/Houston_Person_-_13_-_As_Time_Goes_By.mp3"
    
    scene bg wip
    with fade
    
    show stray normal at midleft
    with dissolve
    
    s "Time to check out my phone!"
    
    show kitsune giggle at midright
    with dissolve
    
    k "{i}You'll have to hang up first to do that, though...{/i}"
    
    window hide
    hide kitsune with dissolve
    
    $ renpy.pause(0.5)
    
    show stray normal at left
    with move
    
    ## Add cellphone screen here
    show phone at phone_pickup

    $ renpy.pause(0.5)
    play sound "sfx/blop.mp3"
    show screen phone_message_other("kitsune", "this is me testing out text messaging!")
    $ renpy.pause()
    hide screen phone_message_other
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
    $ renpy.pause(0.5)
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
    show screen phone_message_other("Kitsune", "that's your thing, right")
    $ renpy.pause()
    hide screen phone_message_other
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
    hide phone

    $renpy.pause(0.2)
    jump continues    
        
##Hide cellphone screen

    
    
label continues:
    window show
    s "My mom is great."
    return 