# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lorekeeper")


label start:

    scene bg room

    show eileen happy

    "Make sure you check out 'script.rpy', 'category.rpy' and 'people.rpy'."

    "The codex has been added to the quick menu so you can check changes while you play."

    l "Welcome, welcome to the Great Library of the Void."

    l "Would you like to know about someone particular? My dear friend {a=showmenu:zack}Zack{/a} perhaps? Or that strange man {a=showmenu:nelson}Nelson{/a}."

    #-----SHOW HIDDEN ENTRY
    $ persistent.bob = True
    l "But no...you're here about him. {a=showmenu:bob}Bob{/a}. (The codex entry 'Bob' has been added)"

    #-----UPDATE ENTRY
    $ persistent.boblooks = True
    l "I'm sure you've seen him in his funny hats. (Codex entry 'Bob' has been updated.)"

    #-----UPDATE ENTRY
    $ persistent.bobbackground = True
    l "He came from an unknown, distant land. He just appeared one day! Now he does our taxes. (Codex entry 'Bob' has been updated once again.)"

    l "Can you live with this information until the day you die?"

    menu:

        "Forget everything about Bob. It's too much for me.":
            $ persistent.bob = False
            $ persistent.boblooks = False
            $ persistent.bobbackground = False

        "Forget where Bob came from. I'm not interested in that.":
            $ persistent.bobbackground = False

        "He wears *funny hats*? No, I don't want to know about that.":
            $ persistent.boblooks = False

        "I'm good, let's end this.":
            l "If you wish so. Persist in the doomed world you have created."

    l "That's all the time I've had to chat with you. Until next time!"


    return
