# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

image phone = "images/phone/bustedphone.png"
image bg wasteland = "images/wasteland.jpg"

image eileen normal = "images/sylvie_normal.png"
image eileen giggle = "images/sylvie_giggle.png"
image eileen smile = "images/sylvie_smile.png"
image eileen surprised = "images/sylvie_surprised.png"



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
    
    scene bg wasteland
    with fade
    
    show eileen normal
    with dissolve

    e "Time to check out my phone!"
    
    window hide
    
    ## Add cellphone screen here
    show phone at phone_pickup

    $ renpy.pause(0.5)
    show screen phone_message_other("mom", "this is me testing out text messaging!")
    $ renpy.pause()
    hide screen phone_message_other
    show screen phone_sticker_other("ritsu")
    $ renpy.pause(0.5)
    call screen phone_reply("what??","nobreakfast","ew, anime","nobreakfast")
    
    label nobreakfast:
    hide screen phone_sticker_other
    
    $ renpy.pause(0.5)
    show screen phone_message_me("Me", "will you")
    $ renpy.pause(0.5)
    hide screen phone_message_me
    show screen phone_message_me("Me", "stop")
    $ renpy.pause(0.5)
    hide screen phone_message_me
    show screen phone_message_me("Me", "sending me these GODDAMN stickers")
    $ renpy.pause()

    hide screen phone_message_me
    $ renpy.pause(0.1)

    show screen phone_message_other("mom", "ok")
    $ renpy.pause()

    hide screen phone_message_other
    hide phone

    $renpy.pause(0.2)
    jump continues    
        
##Hide cellphone screen

    
    
label continues:
    
    window show
    e "My mom is great."
    return