def NewGame():
    global pronoun
    global Pronoun
    global name
    global gend
    global proff
    global inv1
    global inv2
    global inv3
    global inv4
    global inv5
    global inv6
    global inv7
    global inv8
    global inv9
    global inv0
    global HP
    global gameFlag
    global roomNo
    global rooms
    global lootNo
    global monsterNo
    global monster
    print "You awake upon a small bed, loosly swathed in ratty sheets."
    print "Stirring you see a figure in the corner, loosely garbed in torn robes."
    print "They look at you and greet you, introducing themself as Urah."

    name = raw_input("They then ask you for your name. You awnswer : ")

    print "The figure aplogizes, your clothes were destroyed when they found you"
    print "So they outfitted you with a standard set of leather armour"

    while not (gend in ["MALE","Male","male","M","m","FEMALE","Female","female","F","f","OTHER","Other","other","O","o"]):
        gend = raw_input("you see yourself wearing a standard leather for (Male/Female/Other) : ")
        if gend in ["MALE","Male","male","M","m"]:
            pronoun = "he"
            Pronoun = "He"
        elif gend in ["FEMALE","Female","female","F","f"]:
            pronoun = "she"
            Pronoun = "She"
        elif gend in ["OTHER","Other","other","O","o"]:
            pronoun = "they"
            Pronoun = "They"
        else :
            print "Entry not recognized"

    print "After some food and drink you feel well enough to try and escape the dungeons."

    while not proff in ["Warrior","warrior","W","w","Rogue","rogue","R","r"]:
        proff = raw_input("With some effort you gather enough equipment to fight as a (Rouge/Warrior) : ")
        if proff in ["Warrior","warrior","W","w"]:
            inv1 = 1
            inv2 = 2
            inv3 = 3
            HP = 2000
            proff = "Warrior"
        elif proff in ["Rogue","rogue","R","r"]:
            inv1 = 1
            inv2 = 2
            inv3 = 3
            HP = 1000
            proff = "Rogue"
        else :
            print "Entry not recognized"
