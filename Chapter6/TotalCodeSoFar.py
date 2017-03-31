from random import randrange

inv1 = inv2 = inv3 = inv4 = inv5 = inv6 = inv7 = inv8 = inv9 = inv0 = 0


lootNo = 6
loot = [
#ID,Name,Description,Duration,Damage
[0,"Empty","Your inventory slot is empty",0,0],
[1,"Health Potion","This potion will aid in your recovery, increasing your HP by 250 points",1,-250],
[2,"Status Potion","This potion will purge you of any status effects. Unfortunately, it can take a while to kick in.",1,0],
[3,"Poison","This special poison will cause your blows to deal damage over time. The vial has enough for ten hits.",10,10],
[4,"Pyrotheum","This liquid is a special oil, concocted such that it will set whatever it hits of fire. The ampule contains enough to last five hits.",5,25],
[5,"Cryotheum","A strange crystaline paste. On contact with another object it will immediately cause it to freeze. The flask contains enough to last for five hits.",5,25],
[6,"Reflex Enhancer","A serum designed to allow you to dodge attacks even if you are distracted",3,0]
] #if you change this, remember to update the fight code!

monsterNo = 4
monster = [
[0,#ID
"Nothing",#name
"ASCII (not implemented)",#art
"This entry is a placeholder, to be used if creating a persistent map",1,#description
0,[#number of attacks
["0","The monster does nothing",0,0,0]],#attack
[1],#strength
[3,4,5]],#weakness
[1,#ID
"Kobold",#name
500,#HP
"ASCII (not implemented)",#art
"A brutish little beast. These creatures will attemmpt to kill you in search of even the smallest morsels of food",#description
1,[#number of attacks
[0,"The monster does nothing",1,0,0],
[1,"The kobold rushes at you, striking you with it's fists!",4,5,0]],#attack - number,description, attempts, damage, satus effect
[],#strength
[]],#weakness
[2,#ID
"Skeleton",#name
250,#HP
"ASCII (not implemented)",#art
"The remains of a body posessed by a vengful spirit. As with all undead it has an immense hatered of all living beings",#description
2,[#number of attacks
[0,"The Monster does nothing",1,0],
[1,"The skeleton charges at you, bringing it's arm down with all the strength it can muster!",1,20,0],#attack - number,description, attempts, damage, satus effect
[2,"The skeleton lets loose a flurry of swipes with it's bony fingers!",5,5,5]],#attack - number,description, attempts, damage, satus effect
[3],#strength
[4]],#weakness
[3,#ID
"Ogre",#name
1250,#HP
"ASCII (not implemented)",#art
"A swollen, missshapen being. They are beleived to be the corpses of adventurers corrupted by the dungeon. Their sweat is highly toxic.",#description
3,[#number of attacks
[0,"The Monster does nothing",1,0],
[1,"The Ogre grabs at you, attempting to crush you!",1,50,3],#attack - number,description, attempts, damage, satus effect
[2,"The creature swings at you with it's fists!",2,20,3],#attack - number,description, attempts, damage, satus effect
[3,"The creature roars and flails it's arms wildly!",5,10,3]],#attack - number,description, attempts, damage, satus effect
[4,5],#strength
[3]],#weakness
[4,#ID
"Goblin",#name
750,#HP
"ASCII (not implemented)",#art
"Somewhat conniving, these creatures weild poisonous daggers and carry firebombs.",#description
4,[#number of attacks4
[0,"The Monster does nothing",1,0],
[1,"The creature thows a firebomb at you!",1,10,4],#attack - number,description, attempts, damage, satus effect
[2,"The creature swipes at you with it's blade",4,2,3],#attack - number,description, attempts, damage, satus effect
[3,"The goblin stabs at you with great intensity",1,15,4],#attack - number,description, attempts, damage, satus effect
[4,"The gobline prepares to dodge",1,0,-6]],#attack - number,description, attempts, damage, satus effect
[],#strength
[]],#weakness
]


def PrintInventory():
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
    global loot
    global monsterNo
    global monster

    print "========================================"
    print "Slot 1 " + loot[int(inv1)][1]
    print "   - " + loot[int(inv1)][2]
    print "-----------------------------------------"
    print "Slot 2 " + loot[int(inv2)][1]
    print "   - " + loot[int(inv2)][2]
    print "-----------------------------------------"
    print "Slot 3 " + loot[int(inv3)][1]
    print "   - " + loot[int(inv3)][2]
    print "-----------------------------------------"
    print "Slot 4 " + loot[int(inv4)][1]
    print "   - " + loot[int(inv4)][2]
    print "-----------------------------------------"
    print "Slot 5 " + loot[int(inv5)][1]
    print "   - " + loot[int(inv5)][2]
    print "-----------------------------------------"
    print "Slot 6 " + loot[int(inv6)][1]
    print "   - " + loot[int(inv6)][2]
    print "-----------------------------------------"
    print "Slot 7 " + loot[int(inv7)][1]
    print "   - " + loot[int(inv7)][2]
    print "-----------------------------------------"
    print "Slot 8 " + loot[int(inv8)][1]
    print "   - " + loot[int(inv8)][2]
    print "-----------------------------------------"
    print "Slot 9 " + loot[int(inv9)][1]
    print "   - " + loot[int(inv9)][2]
    print "-----------------------------------------"
    print "Slot 0 " + loot[int(inv0)][1]
    print "   - " + loot[int(inv0)][2]
    print "========================================="

def LootRoll():
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
    result = randrange(1,lootNo,1)
    print ("You found a " + loot[int(result)][1] + " where would you like to store it? putting something in a filled slot will destroy the previous object.")
    PrintInventory()
    chooseSlot = raw_input("Slot : ")
    if chooseSlot in ["Slot 1","slot 1","Slot1","slot1","1"]:
        inv1 = loot[result][0]
    if chooseSlot in ["Slot 2","slot 2","Slot2","slot2","2"]:
        inv2 = loot[result][0]
    if chooseSlot in ["Slot 3","slot 3","Slot3","slot3","3"]:
        inv3 = loot[result][0]
    if chooseSlot in ["Slot 4","slot 4","Slot4","slot4","4"]:
        inv4 = loot[result][0]
    if chooseSlot in ["Slot 5","slot 5","Slot5","slot5","5"]:
        inv5 = loot[result][0]
    if chooseSlot in ["Slot 6","slot 6","Slot6","slot6","6"]:
        inv6 = loot[result][0]
    if chooseSlot in ["Slot 7","slot 7","Slot7","slot7","7"]:
        inv7 = loot[result][0]
    if chooseSlot in ["Slot 8","slot 8","Slot8","slot8","8"]:
        inv8 = loot[result][0]
    if chooseSlot in ["Slot 9","slot 9","Slot9","slot9","9"]:
        inv9 = loot[result][0]
    if chooseSlot in ["Slot 0","slot 0","Slot0","slot0","0"]:
        inv0 = loot[result][0]
      

def Fight():
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
    result = randrange(1,monsterNo,1)

    heroStatus = []
    monsterStatus = []
    attackStatus = []

    heroDodge = False
    monsterDodge = False
    heroDefend = False
    monsterDefend = False

    print "You are attacked by a "+monster[int(result)][1]
    #insert the ASCII here if you have it!
    print "       - " + monster[int(result)][4]

    monsterHP = int(monster[int(result)][2])

    while True:
        monsterAttack = randrange(1,monster[int(result)][5]+1,1)
        for i in range(monster[int(result)][6][int(monsterAttack)][2]):
            strikeChance = randrange(0,5)
            if(strikeChance<4):
                if heroDodge:
                    dodge = randrange(1,10)
                    heroDodge = False
                    if (dodge<2):
                        HP = HP - monster[int(result)][6][int(monsterAttack)][3]
                        if (HP<1):
                            print "You died"
                            gameFlag = False
                            return
                        if (monster[int(result)][6][int(monsterAttack)][4]<1):
                            monsterStatus.append([0-monster[int(result)][6][int(monsterAttack)][4],loot[0-monster[int(result)][6][int(monsterAttack)][4]][3],loot[0-monster[int(result)][6][int(monsterAttack)][4]][4]])
                        elif(monster[int(result)][6][int(monsterAttack)][4]>0):
                            heroStatus.append([monster[int(result)][6][int(monsterAttack)][4],loot[monster[int(result)][6][int(monsterAttack)][4]][3],loot[monster[int(result)][6][int(monsterAttack)][4]][4]])
                elif heroDefend:
                    heroDefend = False
                    HP = HP - (monster[int(result)][6][int(monsterAttack)][3]/10)
                    if (HP<1):
                        print "You died"
                        gameFlag = False
                        return
                    if (monster[int(result)][6][int(monsterAttack)][4]<1):
                        monsterStatus.append([0-monster[int(result)][6][int(monsterAttack)][4],loot[0-monster[int(result)][6][int(monsterAttack)][4]][3],loot[0-monster[int(result)][6][int(monsterAttack)][4]][4]])
                    elif(monster[int(result)][6][int(monsterAttack)][4]>0):
                        heroStatus.append([monster[int(result)][6][int(monsterAttack)][4],loot[monster[int(result)][6][int(monsterAttack)][4]][3],loot[monster[int(result)][6][int(monsterAttack)][4]][4]])
                else:
                    HP = int(HP) - monster[int(result)][6][int(monsterAttack)][3]
                    if (HP<1):
                        print "You died"
                        gameFlag = False
                        return
                    if (monster[int(result)][6][int(monsterAttack)][4]<1):
                        monsterStatus.append([0-monster[int(result)][6][int(monsterAttack)][4],loot[0-monster[int(result)][6][int(monsterAttack)][4]][3],loot[0-monster[int(result)][6][int(monsterAttack)][4]][4]])
                    elif(monster[int(result)][6][int(monsterAttack)][4]>0):
                        heroStatus.append([monster[int(result)][6][int(monsterAttack)][4],loot[monster[int(result)][6][int(monsterAttack)][4]][3],loot[monster[int(result)][6][int(monsterAttack)][4]][4]])




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
