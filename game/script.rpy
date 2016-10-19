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

image stray normal = "images/sprites/body-sprite-1.png"

image kitsune giggle = "images/sprites/kitsune-phone.png"



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

# The game starts here.
label start:
    
    scene bg wip
    with fade
    
    show stray normal
    with dissolve
    
    s "Time to check out my phone!"
    
    show kitsune giggle at right
    with dissolve
    
    k "{i}You'll have to hang up first to do that, though...{/i}"
    
    window hide
    hide kitsune 
    
    ## Add cellphone screen here
    show phone at phone_pickup

    $ renpy.pause(0.5)
    show screen phone_message_other("kitsune", "this is me testing out text messaging!")
    $ renpy.pause()
    hide screen phone_message_other
    show screen phone_sticker_other("kitsune", "ritsu")
    $ renpy.pause(0.5)
    call screen phone_reply("what??","nobreakfast","ew, anime","nobreakfast")
    
    label nobreakfast:
    hide screen phone_sticker_other
    
    $ renpy.pause(0.5)
    show screen phone_message_me("will you")
    $ renpy.pause(0.5)
    hide screen phone_message_me
    show screen phone_message_me("stop")
    $ renpy.pause(0.5)
    hide screen phone_message_me
    show screen phone_message_me("sending me these GODDAMN stickers")
    $ renpy.pause()

    hide screen phone_message_me
    $ renpy.pause(0.1)

    show screen phone_message_other("ohms", "ok")
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