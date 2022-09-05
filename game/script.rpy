# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sean = Character("Sean")
define luke = Character("Luke") 
define david = Character("David") 
define felicity = Character ("Felicity")
define julian = Character("Julian")
define riley = Character("Riley")
define mel = Character("Melissa") 
define prath = Character("Prath")
define johan = Character("Johan")
define mitch = Character("Mitch")
define god = Character("William Lee")

define you = Character("You")
define you_name = Character("[your_name]")
define unknown = Character("???")

# TODO: David Route First.

# Key for Colors:
# {color=#3cdfff} is for inner thoughts
# {color=#ffd700} is for important mystery elements
# 
#
#
#
#

init python:
    
    def addAffection(name):
        if (name == "Luke"):
            if not hasattr(store, "luke_affection"):
                luke_affection = 1
            else:
                luke_affection +=1
        elif (name == "Julian"):
            if not hasattr(store, "julian_affection"):
                julian_affection = 1
            else:
                julian_affection +=1
        elif (name == "Sean"):
            if not hasattr(store, "sean_affection"):
                sean_affection = 1
            else:
                sean_affection +=1
        elif (name == "David"):
            if not hasattr(store, "david_affection"):
                david_affection = 1
            else:
                david_affection +=1
        elif (name == "Felicity"):
            if not hasattr(store, "felicity_affection"):
                felicity_affection = 1
            else:
                felicity_affection +=1
        elif (name == "Mel"):
            if not hasattr(store, "mel_affection"):
                mel_affection = 1
            else:
                mel_affection +=1
        elif (name == "Johan"):
            if not hasattr(store, "johan_affection"):
                johan_affection = 1
            else:
                johan_affection +=1
        elif (name == "Mitch"):
            if not hasattr(store, "mitch_affection"):
                mitch_affection = 1
            else:
                mitch_affection +=1
        elif (name == "God"):
            if not hasattr(store, "god_affection"):
                god_affection = 1
            else:
                god_affection +=1
        else:
            if not hasattr(store, "prath_affection"):
                prath_affection = 1
            else:
                prath_affection +=1

    def get_current_scene():
        img_list = []
        tags = renpy.get_showing_tags()
        for i in list(tags): 
            tag_name = i
            atrb = renpy.get_ordered_image_attributes(i)
            for a in atrb:
                tag_name += ' ' + a
            img_list.append(tag_name)
        return img_list[0]

    def label_callback(name, abnormal):
        store.current_label = name

    def playAudio(file_name):
        renpy.play("audio/"+file_name)

    config.label_callback = label_callback
        
    toggle_inv_dict = {
        "ch1_part1_reader_room" : "ch1_part1_reader_room_inv",
        "ch1_part1_hallway_one" : "ch1_part1_hallway_one_inv",
        "ch1_part1_hallway_two" : "ch1_part1_hallway_two_inv",
        "ch1_part1_hallway_three" : "ch1_part1_hallway_three_inv"
    }

init:
    $ config.keymap['toggle_skip'].remove('K_TAB')
    
    transform zoom_half:
        zoom 0.5
    transform blur_bg:
        blur 10
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ your_name = "Prath"
    $ your_gender = "M"
    jump ch1_part1_hallway_three
    scene classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    unknown "Welcome to DanganPineapple, a fangame 'inspired' by Danganronpa, based on the hit discord server Pineapple Kingdom."
    unknown "This is a demo of chapter 1, and was made in a week and is therefore pretty fucking shit."
    unknown "All characters are only loosely inspired by real people. You'll realize this the further you get into the game."
    unknown "Please enjoy the game from here onwards (or else). I did put effort into it."

    jump prologue
    return

label prologue:

    python:
            your_name = renpy.input("You, reader, what is your name?", length=32)
            your_name = your_name.strip()
            if not your_name:
                your_name = "Prath"

            your_gender = renpy.input("And you, [your_name], what is your gender? Please answer in M or F.", length=1)
            if not your_gender:
                your_gender = "M"
            if your_gender != "M" or your_gender != "F":
                your_gender = "M"

    scene server_empty
    you "So this is the Pineapple Kingdom, huh..?"
    you "Honestly I'm not really sure why I decided to join this server but.."
    you "I was invited by Luke last night here, after we played tons of ranked games together."
    you "No offense to him but despite having a million points on Pyke he was only so-so."
    you "But hey! Regardless of that, it was still a lot of fun."
    you "He asked me to join the VC when I want to play with him again."
    you "I don't really have anything better to do with my time, so might as well?"

    scene reader_vc_alone

    you "I'm here.. but now what?"
    you "Do I awkwardly wait till he joins?"
    unknown "*20 minutes later*"
    you "It has been a while and he has yet to join.."
    you "*sigh* Do I go back to staring at the wall out of boredom?"

    scene luke_in_afk
    you "Oh wait.. is that.."
    you "Is that Luke..?\nIn the afk channel..?"

    scene luke_vc_talking
    play sound "audio/SFX/discord join.mp3"
    luke "Oh hey! You're the person I duo queue'd with last night, didn't I?"
    scene you_talking_luke
    you "Uhh yeah! That's me."
    you "And on a different note were you just in the afk channel?"
    scene luke_vc_talking
    unknown "Oh yeah haha I didn't realize I was there. I was wondering why you weren't replying."
    scene you_talking_luke
    you "Why I wasn't-"
    you "How long were you in the afk channel for?"
    scene luke_vc_talking
    luke "Oh, not too long, just about 20 minutes?"
    scene you_talking_luke
    you "Twenty minutes!? So did you tried to the same VC as me when I joined, except you ended up joining the afk channel,"
    you "And you only realized now!?"
    scene luke_vc_talking
    luke "Yes I did, and you should be careful about how you talk to me."
    luke "Not even my discord kittens ever dare be rude to me, you know?"
    scene you_talking_luke
    you "Oh, sorry, I didn't mean to be rude."
    scene luke_vc_talking
    luke "That's alright, I forgive you!"
    luke "Eitherway, welcome to Pineapple Kingdom!"
    luke "I'm the owner of this server, you know?"
    scene you_talking_luke
    you "I- I do."
    you "So, um, you said that you'll introduce others to me today?"
    scene luke_vc_talking
    luke "Oh yeah, unfortunately no one else is online right now."
    luke "Allow me to tell you about others though."
    luke "Who would you like to know about first?"

    jump ch1_introductions
    return

label ch1_introductions:

    scene luke_vc_talking
    menu self_introductions:
        "Sean" if not hasattr(store, "sean_introduced"):
            $ sean_introduced = True
            show sean
            luke "Him? That is Sean, and I do love his profile picture's thick curves. I mean-"
            luke "Uhm uhm sorry. About him, I've known him for a very long time. I've known him for a long time."
            luke "He's a very chill guy who won't do anything wrong and would love to be your friend!"
            luke "Although I'm pretty sure he calls himself the"
            luke "ULTIMATE MONOKUMA"
            jump ch1_introductions
        
        "David" if not hasattr(store, "david_introduced"):
            $ david_introduced = True
            show david
            luke "Ah! David! My beloved <3"
            luke "I believe he is a hardstuck mastery 6 500k points on yasuo player."
            luke "He's a really fun person to talk to! Although he has a funny way of talking at times. You'll see."
            luke "I believe he was the"
            luke "ULTIMATE GAMER"
            jump ch1_introductions

        "Luke" if not hasattr(store, "luke_introduced"):
            $ luke_introduced = True
            luke "Me? I'm not one to talk about myself, and besides,"
            luke "There's really not much to talk about other than me being the admin of this discord server."
            jump ch1_introductions

        "Riley" if not hasattr(store, "riley_introduced"):
            $ riley_introduced = True
            show riley
            luke "You're interested in *the* Riley?"
            luke "I believe we call him our resident drug addict."
            luke "You can often find him high in our VCs, always smoking another pack of weed."
            luke "And obviously, he's the"
            luke "ULTIMATE DRUG ADDICT"
            jump ch1_introductions

        "Felicity" if not hasattr(store, "felicity_introduced"):
            $ felicity_introduced = True
            show felicity
            luke "Oh, Felicity?"
            luke "You'll enjoy talking to her. I believe her profile picture tells you need to know."
            luke "She says that she just 'kins' Rantaro but, don't tell her I said this, I believe her to be pretty much a simp."
            luke "And thus, she's the"
            luke "ULTIMATE SIMP"
            jump ch1_introductions

        "Julian" if not hasattr(store, "julian_introduced"):
            $ julian_introduced = True  
            show julian
            luke "Curious about Julian? Well I'll ask you this-"
            luke "Do you know who it is on his profile picture?"
            menu:
                "Yes":
                    luke "Oh that's surprising!"
                    luke "..Or not, considering you're now a part of Pineapple Kingdom."
                    $ addAffection("Julian")
                "No":
                    luke "Don't worry that's normal. It's Roboco from HoloLive!"
            luke "But yes, he absolutely loves HoloLive!"
            luke "Tell you what, if you can tell me who his favorite VTuber is, I'll give you a secret surprise ;)"
            luke "And before I forget to mention, he's the"
            luke "ULTIMATE VTUBER APPRECIATOR"
            jump ch1_introductions
        
        "Johan" if not hasattr(store, "johan_introduced"):
            $ johan_introduced = True
            show johan
            luke "In short, Johan's a really wholesome person."
            luke "He cares about everyone more than anyone else."
            luke "There's no one here who can dislike Johan. Which pretty much makes him the"
            luke "ULTIMATE DAD"
            jump ch1_introductions

        "Melissa" if not hasattr(store, "mel_introduced"):
            $ mel_introduced = True
            show mel
            luke "Melissa! She's a very nice person who absolutely adores animals."
            luke "She often uploads pictures of cats and dogs. It's awesome!"
            luke "Needless to say, she's the"
            luke "ULTIMATE ANIMAL LOVER"
            jump ch1_introductions

        "Mitch" if not hasattr(store, "mitch_introduced"):
            $ mitch_introduced = True
            luke "Mitch is our resident shitposter."
            luke "You'll often see him posting random shit everywhere."
            luke "From the most cursed shit to the weirdest posts, he's got everything."
            luke "Obviously, he's the"
            luke "ULTIMATE SHITPOSTER"
            jump ch1_introductions

        "William Lee" if not hasattr(store, "god_introduced"):
            $ god_introduced = True
            luke "He.. is a bit of a weirdo."
            luke "He gets everyone to call him 'God' for some reason."
            luke "And everyone goes along you know? We feel bad for him. It'd be cool for you to go along as well."

            luke "Clearly, he's the"
            luke "ULTIMATE GOD COMPLEX"
            jump ch1_introductions

    luke "So that's with the introductions." 
    luke "Does anyone in particular someone you'd like to know more about?"
    you "No.. not really."
    luke "Really? Well, that's all I can tell you about others for now."
    luke "It's best if you talk to them yourself!"
    luke "A majority of the rest of the people on this server are my kittens."
    luke "And I doubt you'd wanna know about anyone them anyway!"
    luke "Oh, that reminds me, I need to go to talk to xXCuteKittyXx. Catch you later!"
    you "And he's gone..? xXCuteKittyXx..? Do I even wanna know?"
    you "*sigh*\nRegardless, it was good knowing about the people from this server."
    you "I wonder if I'll ever get to meet them."
    you "Eitherway, I should go crash now."
    you "I couldn't play League with him right now anyway, so there really isn't any point in me staying up anymore."
    you "..."
    you "..."

    scene black_bg
    you "{color=#ff0000}Little did I know, this was the last time I'd feel the comfort of my bed.{/color}"
    play movie "images/ch1_introduction.webm"
    $ renpy.pause (10.0, hard=True)

    jump ch1_part1
    return

label ch1_part1:
    
    scene black_bg

    $ renpy.pause (2.0, hard=True)

    unknown "Hey, wake up."
    unknown "Hey, wake up, will you?"
    unknown "Hey, you, wakie wakie!"
    unknown "If you don't wake up soon I will have to do to you what I do to my discord kittens."

    scene reader_room_ch1
    with Dissolve (1.5)
    
    scene black_bg
    with Dissolve (0.5)

    scene reader_room_ch1
    with Dissolve (1.5)

    you "Morning.. wait who's voice is this!?"

    show luke

    unknown "Now now, that's hurtful. You don't remember my voice?"
    luke "We literally talked less than 24 hours ago. It's me, Luke!"
    you "Luke? From Pineapple Kingdom?"
    play sound "audio/Voicelines/Luke/owntheserver.mp3"
    luke "Yup that's me! And you do remember that I own the server, right?"
    you "Um.. yup I remember it all well."
    you "Eitherway, that doesn't explain what you are doing in my room!?"
    luke "Your room..?"
    luke "I guess you haven't looked around properly yet, have you?"
    you "{color=#3cdfff} He's right, this room.. doesn't feel like it's mine.{/color}"
    you "{color=#3cdfff} I really should look around. {/color}"
    hide luke
    window hide
    pause
    window show
    you "{color=#3cdfff} No way in hell does this look like my room. {/color}"
    show luke
    you "Where am I!? Did you kidnap me or something!?"
    luke "Oh, rest assured, I have done no such thing."
    luke "In fact, I myself seem to be in a similar situation as you."
    you "What do you mean..?"
    luke "What I mean is that I went to sleep {color=#ffd700}less than four hours ago{/color} and woke up in a room similar to this."
    # Mention why he knows he woke up four hours ago - because he had a watch
    # But reader's watch has been stolen
    you "What..? Does that mean we've both been kidnapped..?"
    luke "Oh, not just us two. There are some others from Pineapple Kingdom as well!"
    luke "Perfect opportunity for you to meet everyone elif you ask me!"
    you "Wha- No! Do you hear yourself!? This isn't the time to joke around!"
    luke "Well, would you rather have me go in a panic frenzy?"
    luke "\"Oh no! Help! I woke up in a very strange bedroom and I think I'm going to die!!\""
    luke "Do you really think that will help our situation?"
    you "Well.. no.."
    luke "Precisely!"
    luke "So come on now, get out of your bed already! Everyone's waiting for you in the hallway right outside."
    luke "You wanna come on now or take a moment to yourself?"
    menu:
        "Go there with him.":
            $ addAffection("Luke")
            luke "That's what I like to hear!"
            jump ch1_part2
        "Take a moment to yourself.":
            luke "Suit yourself."
            jump ch1_part1_reader_room

    return

label ch1_part1_reader_room:
    window hide
    show screen investigate_mode(current_label)
    call screen reader_room_ch1_inv()
    pause
    jump ch1_part1_reader_room
    return

screen reader_room_ch1_inv():
    imagemap:
        ground "reader_room_ch1.png"
        hotspot (643, 177, 131, 611) action Jump ("ch1_part1_reader_room_door")
        hotspot (1352, 174, 334, 433) action Jump ("reader_room_ch1_window")
        hotspot (1020, 522, 197, 421) action Jump ("reader_room_ch1_washingmachine")
        hotspot (0, 627, 322, 225) action Jump ("reader_room_ch1_posters")
        hotspot (326, 141, 74, 164) action Jump ("reader_room_ch1_clock")
        hotspot (401, 251, 63, 432) action Jump ("reader_room_ch1_cloth")

label ch1_part1_reader_room_inv:
    play movie "images/ch1_reader_room_inv.webm"
    play sound "audio/SFX/investigation_mode.mp3"
    $ renpy.pause(3.0, hard=True)
    jump ch1_part1_reader_room
    return

label ch1_part1_reader_room_door:
    scene reader_room_ch1
    if (hasattr (store, "ch1_part1_interacted_elements_reader_room")):
        if (ch1_part1_interacted_elements_reader_room >= 5):
            scene house_corridor
            with pixellate
            jump ch1_part1_hallway_one
        else:
            you "{color=#3cdfff}I feel like I should investigate my room properly first I leave.{/color}"
            jump ch1_part1_reader_room
    else:
        you "{color=#3cdfff}I feel like I should  my room properly first I leave.{/color}"
        jump ch1_part1_reader_room
    return

label reader_room_ch1_window:
    scene reader_room_ch1
    you "There seems to be really bright light coming out."
    you "And the window.. seems to be sealed shut."
    you "No matter how hard I try to pull it open, it won't buldge."
    if not (hasattr (store, "tried_break_window")):
        you "The window's still gotta be made of glass, right?"
        you "Perhaps I should try to break the window?"
        menu:
            "Yes":
                unknown "*thud*"
                you "Agh!"
                you "This glass does not seem to made off some normal glass."
                you "I did hit it pretty hard, but there's no cracks on it whatsoever."
                $ tried_break_window = True
            "No":
                you "That's probably a better idea."
    if not hasattr(store, "ch1_part1_interacted_elements_reader_room"):
        $ ch1_part1_interacted_elements_reader_room = 1  
    elif not hasattr(store, "ch1_part1_checked_window"):
        $ ch1_part1_interacted_elements_reader_room += 1
    $ ch1_part1_checked_window = True
    jump ch1_part1_reader_room
    return

label reader_room_ch1_cloth:
    scene reader_room_ch1
    if not (hasattr (store, "ch1_part1_checked_cloth")):
        you "What's this odd looking cloth?"
        "*shake* *shake*"
        you "Oh, did something drop while I was trying to move the cloth?"
        you "I wonder what it says."
        you "{color=#ffcccb}Ultimate Loser{/color}..?"
        you "Is that supposed to be my ultimate?"
        you "That's a bit.. grim."
    else:
        you "I already checked the cloth if there was something there."
        you "{color=#ffcccb}Ultimate Loser{/color}..."
        you "Is that really what I am?"
    if not hasattr(store, "ch1_part1_interacted_elements_reader_room"):
        $ ch1_part1_interacted_elements_reader_room = 1  
    elif not hasattr(store, "ch1_part1_checked_cloth"):
        $ ch1_part1_interacted_elements_reader_room += 1
    $ ch1_part1_checked_cloth = True
    jump ch1_part1_reader_room
    return

label reader_room_ch1_posters:
    scene reader_room_ch1
    you "These posters are too faded to make out anything."
    you "Although it would seem like they have different texts in red and green."
    if not hasattr(store, "ch1_part1_interacted_elements_reader_room"):
        $ ch1_part1_interacted_elements_reader_room = 1  
    elif not hasattr(store, "ch1_part1_checked_posters"):
        $ ch1_part1_interacted_elements_reader_room += 1
    $ ch1_part1_checked_posters = True
    jump ch1_part1_reader_room
    return

label reader_room_ch1_clock:
    scene reader_room_ch1
    you "The clock says that it's {color=#ffd700}about 1:50PM.{/color}"
    you "I went to bed at {color=#ffd700}around 10PM..{/color} does that mean I've been asleep for more than 12 hours!?"
    you "There's no way!"
    if not hasattr(store, "ch1_part1_interacted_elements_reader_room"):
        $ ch1_part1_interacted_elements_reader_room = 1
    elif not hasattr(store, "ch1_part1_checked_clock"):
        $ ch1_part1_interacted_elements_reader_room += 1
    $ ch1_part1_checked_clock = True
    jump ch1_part1_reader_room
    return

label reader_room_ch1_washingmachine:
    scene reader_room_ch1
    you "Do we really get our personal washing machines in our rooms!?"
    you "That's crazy! Although judging from the state of this room.."
    unknown "*click* *click*"
    you "Yup, no wonder. This washing machine {color=#ffd700}does not seem to be functional{/color}."
    if not hasattr(store, "ch1_part1_interacted_elements_reader_room"):
        $ ch1_part1_interacted_elements_reader_room = 1  
    elif not hasattr(store, "ch1_part1_checked_washingmachine"):
        $ ch1_part1_interacted_elements_reader_room += 1
    $ ch1_part1_checked_washingmachine = True
    jump ch1_part1_reader_room
    return

label ch1_part1_hallway_one:
    scene house_corridor
    show screen investigate_mode(current_label)
    call screen ch1_part1_hallway_one_inv()
    pause
    jump ch1_part1_hallway_one

label ch1_part1_hallway_one_luke:
    show house_corridor at blur_bg
    show luke at truecenter with dissolve
    luke "Made me wait long enough, didn't you?"
    luke "Jeez, not even my kittens make me wait this long."
    luke ""
    scene house_corridor with dissolve
    jump ch1_part1_hallway_one

label ch1_part1_hallway_one_inv:
    play movie "images/ch1_part1_hallway_one_inv.webm"
    play sound "audio/SFX/investigation_mode.mp3"
    $ renpy.pause(3.0, hard=True)
    pause
    jump ch1_part1_hallway_one

screen ch1_part1_hallway_one_inv():
    modal False
    imagemap:
        ground "house_corridor.png"
        hotspot (1096, 3, 286, 1075) action Jump ("johan_room")
        hotspot (175, 58, 45, 756) action Jump ("david_room")
        hotspot (656, 212, 52, 407) action Jump ("luke_room")
        hotspot (551, 240, 41, 282) action Jump ("ch1_part1_hallway_one_right")
        hotspot (330, 239, 35, 281) action Jump ("ch1_part1_hallway_one_left")
        hotspot (383, 295, 148, 138) action Jump ("hallway_one_window")
        hotspot (1656, 445, 220, 180) action Jump ("ch1_part1_hallway_two")
    vbox xalign 0.15 yalign 0.3:
        imagebutton auto "luke happy %s.png" action Jump ("ch1_part1_hallway_one_luke") at zoom_half

label luke_room:
    scene house_corridor
    if not hasattr(store, "ch1_part2"):
        you "It says that this is.. {color=#ffffe0}Luke's room{/color}."
        you "I don't have any reason to visit the room right now."
    else:
        you "stub - luke's room"
    jump ch1_part1_hallway_one

label david_room:
    scene house_corridor
    if not hasattr(store, "ch1_part2"):
        you "It says that this is.. {color=#ffffe0}David's room{/color}."
        you "I don't have any reason to visit the room right now."
    else:
        you "stub - david's room"
    jump ch1_part1_hallway_one

label johan_room:
    scene house_corridor
    if not hasattr(store, "ch1_part2"):
        you "It says that this is.. {color=#ffffe0} Johan's room {/color}."
        you "I don't have any reason to visit the room right now."
    else:
        you "stub - johan's room"
    jump ch1_part1_hallway_one

label hallway_one_window:
    scene house_corridor
    you "Another window with really bright light coming out of it."
    you "..and it's also sealed shut. Doesn't move an inch."
    if hasattr(store, "tried_break_window"):
        you "I should probably not try to break this window as well."
        you "Really not worth the pain."
    jump ch1_part1_hallway_one

label ch1_part1_hallway_one_left:
    scene house_corridor
    if not hasattr(store, "ch1_part1_hallway_one_talked_to_luke"):
        you "Luke is just standing there. I should probably talk to him first."
        jump ch1_part1_hallway_one
    else:
        scene corridor kitchen
        with pixellate
        jump ch1_part1_hallway_three

label ch1_part1_hallway_one_right:
    scene house_corridor
    if not hasattr(store, "ch1_part1_hallway_one_talked_to_luke"):
        you "Luke is just standing there. I should probably talk to him first."
        jump ch1_part1_hallway_one
    else:
        jump ch1_part1_hallway_two

label ch1_part1_hallway_two:
    if not hasattr(store, "ch1_part1_hallway_one_talked_to_luke"):
        you "Luke is just standing there. I should probably talk to him first."
    else:
        scene house_corridor_inverse
        show screen investigate_mode(current_label)
        call screen ch1_part1_hallway_one_inv()

label ch1_part1_hallway_three:
    scene corridor kitchen
    show screen investigate_mode(current_label)
    call screen ch1_part1_hallway_three_inv()
    pause
    jump ch1_part1_hallway_three

screen ch1_part1_hallway_three_inv():
    imagemap:
        ground "corridor kitchen.png"
        hotspot (1153, 263, 254, 428) action Jump ("ch1_part1_kitchen")
        hotspot (99, 2, 154, 277) action Jump ("ch1_part1_hallway_three_window")
        hotspot (3, 164, 103, 879) action Jump ("ch1_part1_hallway_three_lockers")
        hotspot (103, 223, 132, 704) action Jump ("ch1_part1_hallway_three_lockers")
        hotspot (233, 322, 87, 496) action Jump ("ch1_part1_hallway_three_lockers")
        hotspot (323, 396, 91, 338) action Jump ("ch1_part1_hallway_three_lockers")
        hotspot (414, 439, 46, 245) action Jump ("ch1_part1_hallway_three_lockers")
        hotspot (571, 461, 111, 187) action Jump ("ch1_part1_hallway_three_exit")
        hotspot (920, 447, 20, 227) action Jump ("ch1_part1_hallway_three_washroom_female")
        hotspot (1001, 427, 28, 277) action Jump ("ch1_part1_hallway_three_washroom_male")
        hotspot (1337, 690, 157, 217) action Jump ("ch1_part1_hallway_three_bucket")
        hotspot (1494, 257, 385, 444) action Jump ("ch1_part1_hallway_three_posters")
    vbox xalign 0.45 yalign 0.5:
        imagebutton auto "julian %s.png" action Jump ("ch1_part1_hallway_three_julian") at zoom_half

label ch1_part1_hallway_three_julian:
    show corridor kitchen at blur_bg
    show julian at truecenter with dissolve
    unknown "Hey there! And who might you be?"
    you "M-Me!? I'm [your_name]."
    unknown "Nice to meet you [your_name]!"
    unknown "So I'm gonna guess you also woke up in an unknown room few minutes ago?"
    you "Oh.. yeah, I did! How did you guess?"
    unknown "You aren't the first person to wake up in a situation like this."
    unknown "And Luke told me I should be expecting someone coming this way."
    you "Oh you know about Luke!?"
    unknown "Yeah maybe, I mean, duh?"
    unknown "He's a close friend of mine, and he's also the server owner."
    you "Server owner..? Wait are you part of Pineapple Kingdom as well?"
    unknown "I do think I am!"
    julian "I'm Julian, and my username is 'negative person' on Discord."
    you "Julian! I know a little about you from Luke. I talked to him last night."
    you "Or was it even last night..? It's hard to tell at this point."
    julian "Yeah maybe."
    you "What were you doing out here Julian?"
    julian "Guiding anyone else who comes here to the kitchen."
    julian "On that topic, I was told to tell anyone who maybe comes here to tell them to go inside the kitchen."
    julian "Everyone else is in there as well. Get moving, I'll maybe see you in there."
    you "'Everyone else'..? Just how many people woke up in this place?"
    julian "So far it's {color=#ffd700}11 people{/color}, and {color=#ffd700}everyone seem to be a part of Pineapple Kingdom{/color}."
    julian "Including you, apparently."
    julian "Eitherway, all your other questions can be answered inside. Get moving."

    $ ch1_part1_talked_to_julian = True
    jump ch1_part1_hallway_three

label ch1_part1_hallway_three_inv:
    play movie "images/ch1_part1_hallway_three_inv.webm"
    play sound "audio/SFX/investigation_mode.mp3"
    $ renpy.pause(3.0, hard=True)
    pause
    jump ch1_part1_hallway_three

label ch1_part1_hallway_three_window:
    scene corridor kitchen
    if hasattr(store, "ch1_part1_talked_to_julian"):
        you "Another window with really bright light coming out of it."
        you "It's impossible for me to reach it for now."
        if hasattr(store, "tried_break_window"):
            you "Unlike the window in my room, it's impossible for me to try and break it."
            you "Truly, a shame."
    else:
        you "There's someone standing there. Perhaps I should talk to them first?"
    jump ch1_part1_hallway_three

label ch1_part1_hallway_three_lockers:
    scene corridor kitchen
    if hasattr(store, "ch1_part1_talked_to_julian"):
        you "There's lockers here?"
        you "That's.. weird. It really doesn't make sense for lockers to be here."
        you "Although they all seem to be {color=#ffd700}locked{/color}."
    else:
        you "There's someone standing there. Perhaps I should talk to them first?"
    jump ch1_part1_hallway_three

label ch1_part1_hallway_three_exit:
    scene corridor kitchen
    if hasattr(store, "ch1_part1_talked_to_julian"):
        you "An exit door..?"
        you "Can I use this to exit this place?"
        "*rattle* *rattle*"
        you "Ah.. this door's locked."
        if not hasattr(store, "tried_to_exit"):
            show corridor kitchen at blur_bg
            show julian at truecenter with dissolve
            julian "The door is, perhaps unsurprisingly, locked."
            julian "I'm starting to think that maybe we've been {color=#ffd700}kidnapped{/color}?"
            julian "It's unlikely that kidnappers will leave a door saying \"Exit\" open."
            julian "I can't be too sure though."
            $ tried_to_exit = True
    else:
        you "There's someone standing there. Perhaps I should talk to them first?"
    jump ch1_part1_hallway_three

label ch1_part1_hallway_three_washroom_female:
    scene corridor kitchen
    if hasattr(store, "ch1_part1_talked_to_julian"):
        if your_gender == "F":
            you "I don't have any reason to go to the bathroom right now."
        else:
            you "I.. really shouldn't enter the female bathroom."
    else:
        you "There's someone standing there. Perhaps I should talk to them first?"
    jump ch1_part1_hallway_three

label ch1_part1_hallway_three_washroom_male:
    scene corridor kitchen
    if hasattr(store, "ch1_part1_talked_to_julian"):
        if your_gender == "M":
            you "I don't have any reason to go to the bathroom right now."
        else:
            you "I.. really shouldn't enter the female bathroom."
    else:
        you "There's someone standing there. Perhaps I should talk to them first?"
    jump ch1_part1_hallway_three

label ch1_part1_hallway_three_bucket:
    scene corridor kitchen
    if hasattr(store, "ch1_part1_talked_to_julian"):
        you "There's a bucket here?"
        you "..and why is this bucket empty..?"
        if not hasattr(store, "checked_bucket"):
            show corridor kitchen at blur_bg
            show julian at truecenter with dissolve
            julian "I'm not personally sure why there would be a bucket here.."
            julian "..but perhaps it's because {color=#ffd700}this place was just being cleaned{/color}?"
            julian "No that doesn't make any sense. Why would the bucket be empty then?"
    else:
        you "There's someone standing there. Perhaps I should talk to them first?"
    jump ch1_part1_hallway_three

label ch1_part1_hallway_three_posters:
    scene corridor kitchen
    if hasattr(store, "ch1_part1_talked_to_julian"):
        you "There are some odd posters here."
        you "{color=#ffd700}\"Get your detective skills up! You'll need it!\"{/color}"
        you "{color=#ffd700}\"Or suffer from your lack thereof! Although, that might be just be a lil' harmful.\"{/color}"
        you "{color=#ffd700}\"Hehehehe!\"{/color}"
        you "..I have no idea what this poster is talking about."
    else:
        you "There's someone standing there. Perhaps I should talk to them first?"
    jump ch1_part1_hallway_three


screen investigate_mode(label_name):
    key "K_TAB" action Jump (toggle_inv_dict[label_name])