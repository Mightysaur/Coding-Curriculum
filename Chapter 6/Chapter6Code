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
