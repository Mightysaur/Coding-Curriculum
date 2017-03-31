def LoadString():
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

    validator = True

    while validator:
        saveString = raw_input("enter your save string, entering a faulty save string may crash the game : ")
        #Save string structure : name^gend^proff^HP^inv1|inv2|inv3|inv4|inv5|inv6|inv7|inv8|inv9|inv0

        splitter = saveString.split("^")

        if (len(splitter) == 5):
            name = splitter[0]
            gend = splitter[1]

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
                continue

            proff = splitter[2]
            HP = splitter[3]
            invString = splitter[4]

            invSplitter = invString.split("|")

            if(len(invSplitter) == 10):
                inv1 = invSplitter[0]
                inv2 = invSplitter[1]
                inv3 = invSplitter[2]
                inv4 = invSplitter[3]
                inv5 = invSplitter[4]
                inv6 = invSplitter[5]
                inv7 = invSplitter[6]
                inv8 = invSplitter[7]
                inv9 = invSplitter[8]
                inv0 = invSplitter[9]

                validator = False
            else:
                print "error, try again!"
        else:
            print "error, try again!"

def game():
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
    print "Welcome to the game"
    print "During gamplay, type help if you wish to check your available controls"
    sOrL = raw_input("please type 'new' to start a new game or type 'load' to load a save : ");
    if sOrL in ["NEW","New","new","N","n"]:
        NewGame()
    elif sOrL in ["LOAD","Load","load","L","l"]:
        LoadString()

    while gameFlag:

        roomLoop = True

        roomID = randrange(1,roomNo,1)
        print rooms[roomID][1]

        while roomLoop:
            readAction = raw_input("What do you try and do now? : ")
            splitAction = readAction.split(" ")
            actionSet = set(splitAction).intersection(["Search","search","Investigate","investigate","Examine","examine","Next","next","Hurry","hurry","Avoid","avoid","Fight","fight","Run","run","Help","help","Inventory","inventory","Save","save","Quit","quit"])
            if (len(actionSet)<1):
                print "That input was invald. Try again"
                continue
            action = list(actionSet)[0]
            print action
            if action in ["Search","search","Investigate","investigate","Examine","examine"]:
                event = randrange(1,100)
                if (event <60):
                    LootRoll()
                    roomLoop = False
                elif (event <80):
                    Fight()
                    roomLoop = False
                else:
                    print "You found nothing. Bored, you move on to the next room."
                    roomLoop = False

            elif action in ["Next","next","Hurry","hurry","Avoid","avoid"]:
                event = randrange(1,100)
                if (event <10):
                    Fight()
                    roomLoop = False
                else:
                    print "You make it to the next room without incident."
                    roomLoop = False

            elif action in ["Fight","fight"]:
                event = randrange(1,100)
                if (event <10):
                    print "You found nothing. Bored, you move on to the next room."
                    roomLoop = False
                else:
                    Fight()
                    roomLoop = False

            elif action in ["Run","run"]:
                event = randrange(1,100)
                if (event <10):
                    Fight()
                    roomLoop = False
                else:
                    print "You found nothing. Bored, you move on to the next room."
                    roomLoop = False

            elif action in ["Inventory","inventory"]:
                PrintInventory()

            elif action in ["Help","help"]:
                print "In room scale situations such as this, type in your actions, preferably in small sceneteces. The system will detect keywords such as 'search','invesigate','avoid', 'inventory' or 'fight' and will generate responses accoding to the results. However, the system may get tripped up if multiple keywords are detected."

            elif action in ["Quit","quit"]:
                while True:
                    check = raw_input("Are you sure? (Yes/No)")
                    if check in ["Y","y","Yes","yes"]:
                        roomLoop = False
                        gameFlag = False
                        break
                    elif check in ["N","n","No","no"]:
                        break
                    else:
                        print "Error, invlaid response"

            elif action in ["Save","save"]:
                print name + "^" + gend+ "^"+ proff+ "^"+ str(HP) +"^"+ str(inv1)+ "|" + str(inv2)+ "|"+ str(inv3)+ "|"+ str(inv4)+ "|" + str(inv5)+ "|"+ str(inv6)+ "|"+ str(inv7)+ "|" + str(inv8)+ "|"+ str(inv9)+ "|"+ str(inv0)

            else:
                print "That input was invald. Try for short scentences as the detection of multiple keywords can cause errors do not use any punctuation such as a fullstop or similar, it can interfere with detection"

game() #This runs the game, it's very important!
