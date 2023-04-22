from tkinter import * #Importing tkinter to use the GUI functions it offers.
from PIL import Image, ImageTk #Importing an image handler to work with tkkinter.  If not working install by typing 'pip install Pillow' into your terminal (ctrl+shift+` in VSC).
import files.data.library as lib #importing our library.py

#everytime the character does an incorrect action this function will reset them to the Goblin Smithy room
def death():
    textBox("As your vision fades to black you hear the goblin's distinct muttering in your ear, "
            "it's hard to discern exactly what he's saying due to your fading conciousness, but it doesn't sound pleasant. "
            "You wake up in the Goblin's Smithy. He speaks up \"That was a close one hero, try to be more careful.\"")
    interact(lib.interaction)
    lib.current_room = "DZNTS"
    imageSwap(lib.rooms[lib.current_room]["image"])

#this function is called when entering the exit room
def ending():
    if lib.grape_count == lib.no_grapes: #this is if they found no grapes at all
        sky = "cloudy sky trickling with rain"
        fulfillment = ( "however, you can't help but feel a deep sadness within you. "
                        "Almost as if something was missed. Man you're suddenly craving some Grapes, you could've sworn you "
                        "smelt some in that cave... Oh well!")

    elif lib.grape_count > lib.no_grapes and lib.grape_count < lib.max_grapes: #this is if they have at least 1 grape but not all of them
        sky = "semi-cloudy sky"
        fulfillment = ( "however, you can't help but feel slightly unfulfilled. "
                        "Almost as if something was missed. Man you're suddenly craving some Grapes, good thing you found some, "
                        "you wonder if there wasn't more..? Oh well!")

    elif lib.grape_count == lib.max_grapes: #this is if they have obtained all the grapes possible
        sky = "sunny sky beaming onto you filling you with warmth"
        fulfillment = "in fact! You feel an unbearable happiness welling within you! You can't wait to get home and enjoy your grapes!"

    textBox(f"You survived the arduous cave and are greeted with a {sky}. "
            f"This will be an unforgetable adventure for you no doubt, {fulfillment}")
    end_credits()

#this function is called with the directional buttons
def move_room(direction):
    #the try statement will try moving the player in the direction given wiith the buttons
    #if the player cannot go that way, aka the direction doesn't exist as a key value in the nested dictionary
    #it will cause an error and simply tell the player they cannot go that way
    try:
        #this action will play if the player eters the dark room
        if lib.current_room == "BC0" and direction == "South":
            #if the ruby is obtained and the grape has not yet been obtained the player wil go through this event
            if "Ruby" in lib.current_inventory and "Grape 4" in lib.grapes:
                textBox("The Ruby is glowing dimly, you spot a grape in the corner! The Ruby loses it's glow as you pick up the grape!")
                lib.grapes.remove("Grape 4")
                lib.grape_count += 1
                if lib.grape_count == 1:
                    s = f"You now have 1 Grape!"
                else:
                    s = f"You now have {lib.grape_count} Grapes!"
                textBox(s)
        elif lib.current_room == "C1" and direction == "West":
            ending()
        lib.current_room = lib.rooms[lib.current_room][direction] 
    except:
        textBox("You can't go that way!")
    #after every movement the player will be told what room they are in
    textBox(lib.rooms[lib.current_room]["name"])

#This function is called with the take button
def pickup_items(current_inventory):
    #when they try to pickup an item it checks weither or not you have
    #completed the quest required for the room you are in.
    #if you are not in a room with an item it will run an error and
    #go to the except statement
    try:
        if lib.rooms[lib.current_room]["quest"] == True:
            text ="You obtained", lib.rooms[lib.current_room]["item"] + "!"
            textBox(text)
            current_inventory.append(lib.rooms[lib.current_room]["item"])
            del lib.rooms[lib.current_room]["item"]
            if "Ruby" in current_inventory and lib.current_room=="BA2":
                lib.rooms["BA2"]["image"] = lib.BA2imagec
                lib.rooms[lib.current_room]["name"] = lib.BA2c
            elif "Caliboard" in current_inventory and lib.current_room=="A3":
                lib.rooms["A3"]["image"] = lib.A3imageb
                lib.rooms["A3"]["name"] = lib.A3b
            elif "Pickaxe" in current_inventory and lib.current_room== "DZNTS":
                lib.rooms["DZNTS"]["name"] = lib.DZNTSc
        elif lib.rooms[lib.current_room]["quest"] == False:
            text = lib.incomplete[lib.current_room]
            textBox(text)
        else:
            textBox("There is nothing to pickup!")
    except:
        textBox("There is nothing to pickup!")

#this function is for the Yes/No prompts given by the talking function
#it is called by the Yes/No buttons after the talking function has ran
def groblinisms(talk_DZNTS,y_n):
    #for the goblin smithy this will prioritize the main quest over idle chatter since both are called by the talk button
    if lib.current_room == "DZNTS":
        #if the player has obtained the ruby it will allow the player to pick up the pickaxe
        if lib.goblin_chat_counter == 0:
            #if the player is first talking to the goblin, he will ask his request and give the player a rope
            if y_n == "Yes":
                textBox(lib.dialogue["goblin_dialogue_2"][y_n])
                textBox("You obtained, Rope!")
                lib.current_inventory.append("Rope")
                #managing goblin conversations
                lib.goblin_chat_counter += 1
            else:#else if player says No
                textBox(lib.dialogue["goblin_dialogue_2"][y_n])    
        elif "Ruby" in lib.current_inventory and y_n == "Yes":
            textBox(lib.dialogue["goblin_dialogue_4"][y_n])
            lib.rooms[lib.current_room]["quest"] = True
            lib.current_inventory.remove("Ruby")
        else: #else if no main quests are available and the player says yes to hear the goblin's story
            if y_n == "Yes":
                #if there is stories to be told to the player it will choose at random
                try:
                    textBox(talk_DZNTS[0])
                    talk_DZNTS.pop(0)
                #once the player has heard all the stories from the goblin he will give the player a grape
                except IndexError:
                    if "Grape 1" in lib.grapes:
                        textBox(lib.dialogue["goblin_dialogue_6"])
                        textBox("You've outlistened the goblin! Congrats! You've been given a grape!")
                        lib.grapes.remove("Grape 1")
                        lib.grape_count +=1
                        if lib.grape_count == 1:
                            s = f"You now have 1 Grape!"
                        else:
                            s = f"You now have {lib.grape_count} Grapes!"
                        textBox(s)
                    else:
                        textBox(lib.dialogue["goblin_dialogue_6"])
            else: #else if the player talks to the goblin but says no
                if "Ruby" in lib.current_inventory:
                    textBox(lib.dialogue["goblin_dialogue_4"][y_n])
                else:
                    textBox(lib.dialogue["goblin_dialogue_2"][y_n])
    #if the player chooses to talk to the creature
    elif lib.current_room == "B0BA":
        #if the player says yes to hand the creature the egg
        if y_n == "Yes":
            textBox(lib.dialogue["B0BA_talk"][y_n])
            #removing the egg so this cannot be repeated
            lib.current_inventory.remove("Slime Egg")
            lib.grapes.remove("Grape 3")
            lib.grape_count += 1
            if lib.grape_count == 1:
                s = f"You now have 1 Grape!"
            else:
                s = f"You now have {lib.grape_count} Grapes!"
            textBox(s)
            lib.rooms[lib.current_room]["image"] = lib.B0BAimageb
            imageSwap(lib.rooms[lib.current_room]["image"])
            s = print("",end="")
            interact(s)
        #if the player refuses to give the interested creature the egg
        elif y_n == "No":
                textBox(lib.dialogue["B0BA_talk"][y_n])
                lib.rooms[lib.current_room]["image"] = lib.B0BAimageb
                lib.current_inventory.remove("Slime Egg")
                death()
    #else if the player tries talking in a room without anything it will pass
    else:
        pass
    #this sends the player back to the interact after a yes or no button has been pressed, stops exploitation
    s = print("",end="")
    interact(s)

#This function is called with the use button
def use(current_inventory):
    #if in Chasm room the player can use the rope, if in inventory
    if lib.current_room == "B3": 
        if "Rope" in current_inventory:
            #player can get grape with rope in this room
            if "Grape 2" in lib.grapes:
                textBox("You attach the rope to the start of the bridge and carefully descend into the chasm "
                        "As you reach the bottom your nose tingles, you know that smell anywhere... "
                        "There's a Grape nearby... You obtained a Grape!")
                lib.grape_count += 1
                if lib.grape_count == 1:
                    s = f"You now have 1 Grape!"
                else:
                    s = f"You now have {lib.grape_count} Grapes!"
                textBox(s)
                textBox("You climb back up the rope satisfied with yourself!")
                lib.grapes.remove("Grape 2")
                #placeholder for interact()
                s = print("",end="")
                #sends user back to the previous menu
                default()
            #mood stat isn't a thing, just for fun
            else:
                textBox("There's no more grapes down there! Your mood has decreased!")
        #if the player is not in a room with a use
        else:
            textBox("You have nothing to use here!")
    elif lib.current_room == "C2":
        if "Pickaxe" in current_inventory and lib.wall_break == False:
            textBox("You strike the wall with the pickaxe!... It crumbles before you!")
            lib.rooms["C2"]["image"] = lib.C2imageb
            lib.rooms["C2"]["West"] = "C1"
            lib.rooms["C2"]["name"] = lib.C2b
            imageSwap(lib.rooms[lib.current_room]["image"])
            lib.wall_break = True
        elif "Pickaxe" not in current_inventory:
            textBox("You have nothing to use here!")
        else:
            textBox("You already broke through!")
    #this next section of the function is for stairwells
    elif lib.current_room == "C4":
        textBox("You descend the stairwell!")
        lib.current_room = "BC0"
        textBox(lib.rooms[lib.current_room]["name"])
        default()
    elif lib.current_room == "BC0":
        textBox("You ascend the stairwell!")
        lib.current_room = "C4"
        textBox(lib.rooms[lib.current_room]["name"])
        default()
    else:
        textBox("You have nothing to use here!")
#this is for when the player tries talking in a room without anything to talk to
def no_talk():
    textBox("There is nothing to talk to here!")
    #this will bring back the interact menu
    s = print("",end="")
    interact(s)
#This function is called with the talk button
def talking(current_room):
    #changes the buttons available to the player when used
    talkButton.pack_forget()
    takeButton.pack_forget()
    useButton.pack_forget()
    leaveButton.pack_forget()
    #only gives the player a yes or no button option
    yesButton.pack(side=LEFT, padx=(267,5), pady=(0,15))
    noButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    root.bind('<a>', lambda event:groblinisms(lib.talk_DZNTS,"Yes"))
    root.bind('<s>', lambda event:groblinisms(lib.talk_DZNTS,"No"))
    root.bind('<d>', lambda event:cant())
    root.bind('<e>', lambda event:cant())
    #this next section gives the player a yes/no prompt when in the specified room also depending on items and quests
    #if in goblin smithy
    if lib.current_room == "DZNTS":
        #if there is main quests to be said then it will be prioritized
        if "Ruby" in lib.current_inventory and lib.goblin_chat_counter != 0:
                textBox(lib.dialogue["goblin_dialogue_3"]["Talk"])
                lib.dialogue["goblin_dialogue_3"]["Talk"]=lib.dialogue["goblin_dialogue_3"]["Talk_b"]
        elif lib.goblin_chat_counter == 0:
            #this will complete the main quest if the player has already talked to the goblin
            #this will start the main quest for the player
            textBox(lib.dialogue["goblin_dialogue_1"]["Talk"])
            lib.dialogue["goblin_dialogue_1"]["Talk"] = lib.dialogue["goblin_dialogue_1"]["Talk_b"]
            lib.rooms["DZNTS"]["name"] = lib.DZNTSb
        #if the player does not fulfil the conditions to progress any quest with the goblin it will cause idle chatter to happen
        else:
            textBox(lib.dialogue["goblin_dialogue_5"])
    #if in creature room
    elif lib.current_room == "B0BA":
        #Player must have slime egg to talk with the creature
        if "Slime Egg" in lib.current_inventory:
            textBox(lib.dialogue["B0BA_talk"]["Talk"])
        #if the player has already obtained the grape from the creature
        elif "Grape 3" not in lib.grapes:
            textBox("You shouldn't bother the creature anymore!")
            #this will bring back the interact menu
            s = print("",end="")
            interact(s)
        #if player tries talking to the creature with out the required item
        else:
            textBox("The creature pounces on you imediately!")
            death()
    #Talking in orc room will result in 'death'
    elif lib.current_room == "BA2":
        if lib.rooms[lib.current_room]["quest"] == True:
            no_talk()
        else:
            textBox("Revealing yourself wasn't very smart! the orc turns around to face you...")
            death()
    #talking in Slime room will result in 'death'    
    elif lib.current_room == "BB1":
        if lib.rooms[lib.current_room]["quest"] == True:
            no_talk()
        else:
            textBox("Revealing yourself wasn't very smart! the slime lunges towards you...")
            death()
    #talking in a room without npc/monster will display this essage
    else:
        no_talk()

#This function is called with the attack button
def attack(current_room,current_inventory):
    #attacking the goblin with and without the sword, ultimtely does nothing either way
    if lib.current_room == "DZNTS":
        if "Caliboard" in current_inventory:
            textBox(lib.dialogue["goblin_attack"]["Caliboard"])
        else:
            textBox(lib.dialogue["goblin_attack"]["Fist"])
    elif lib.current_room == "BB1":
        if "Caliboard" in current_inventory:
            #if the slime is dead it does nothing
            if lib.rooms[lib.current_room]["quest"] == True:
                textBox("You strike the ground!... That was fun :)")
            #if the slime is alive it changes to dead
            else:
                textBox(lib.dialogue["slime_attack"])
                lib.rooms[lib.current_room]["name"] = lib.BB1b
                lib.rooms[lib.current_room]["quest"] = True
                lib.rooms[lib.current_room]["East"] = "BB2"
                lib.rooms[lib.current_room]["image"] = lib.BB1imageb
                imageSwap(lib.rooms[lib.current_room]["image"])
        else:
            textBox(lib.dialogue["weaponless"])
            death()
            
    elif lib.current_room == "B0BA":
        textBox(lib.dialogue["B0BA_attack"])
        death()

    elif lib.current_room == "BA2":
        if "Caliboard" in current_inventory:
            if lib.rooms[lib.current_room]["quest"] == True:
                textBox("You strike the ground!... That was fun! :)")
            else:
                textBox(lib.dialogue["orc_attack"])
                lib.rooms[lib.current_room]["quest"] = True
                lib.rooms[lib.current_room]["image"] = lib.BA2imageb
                lib.rooms[lib.current_room]["name"] = lib.BA2b
                imageSwap(lib.rooms[lib.current_room]["image"])
        else:
            death()

    else:
        textBox("You strike the ground!... That was fun :)")

#Function that sets up the title screen for the game.
def titleScreen():
    titleCanvas.pack()
    newGameButton.pack(side=TOP, pady=(200,0))
    quitButtonTitle.pack(side=TOP, pady=(5,0))
#function for importing a text string into the Text widget without allowing the player to edit the box.
def textBox(x): 
    textLog.configure(state=NORMAL)
    try:
        textLog.insert(END, "\n\n"+x, 'center')
    except:
        try:
            textLog.insert(END, "\n\n"+", ".join(x), 'center')
        except:
            pass
    textLog.yview_moveto(1.0)
    textLog.configure(state=DISABLED)
#function for importing a desired image into any given scene.
def imageSwap(x): 
    x = ImageTk.PhotoImage(Image.open("files\\images\\%s" %x))
    displayCanvas.configure(image=x)
    displayCanvas.image=x
#function for setting the default actions bar
def default():
    subCanvas.pack(pady=0)
    displayCanvas.pack(side=LEFT, pady=0, padx=(100,0))
    displayFrame.pack(side=TOP, fill=X, pady=0)
    textLogFrame.pack(fill=BOTH, pady=0)
    textCanvas.pack(pady=0)
    actionsFrame.pack(fill=BOTH, pady=0)
    actionsCanvas.pack(pady=0)
    textLog.pack(side=LEFT, pady=0, padx=(107, 0)) #packing the text log.
    scrollbar.pack(side=LEFT, fill=Y, pady=0)
    yesButton.pack_forget()
    noButton.pack_forget()
    talkButton.pack_forget()
    leaveButton.pack_forget()
    useButton.pack_forget()
    takeButton.pack_forget()
    northButton.pack(side=LEFT, padx=(55,5), pady=(0,15))
    westButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    southButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    eastButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    interactButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    attackButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    invButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    quitButton.pack(side=RIGHT, padx=(0,16), pady=(0,200))
    root.bind('<w>', lambda event:buttons(move_room("North"), lib.rooms[lib.current_room]["image"]))
    root.bind('<a>', lambda event:buttons(move_room("West"), lib.rooms[lib.current_room]["image"]))
    root.bind('<s>', lambda event:buttons(move_room("South"), lib.rooms[lib.current_room]["image"]))
    root.bind('<d>', lambda event:buttons(move_room("East"), lib.rooms[lib.current_room]["image"]))
    root.bind('<e>', lambda event:interact(lib.interaction))
    root.bind('<r>', lambda event:buttons(attack(lib.current_room,lib.current_inventory), lib.rooms[lib.current_room]["image"]))
    root.bind('<f>', lambda event:buttons(pickup_items(lib.current_inventory), lib.rooms[lib.current_room]["image"]))
    root.bind('<q>', lambda event:buttons(lib.current_inventory, lib.rooms[lib.current_room]["image"]))
#function that sets up the game opening
def intro():
    titleCanvas.pack_forget()
    textLog.configure(state=NORMAL)
    imageSwap(lib.rooms[lib.current_room]["image"])
    textLog.insert(END, ("Welcome to the Adventure Cave!  After travelling far, you found yourself in a legendary cave.\nBefore long however, you slipped and the path behind you caved in.\nYou must find your way out!\n" + lib.rooms[lib.current_room]["name"]), 'center')
    textLog.configure(state=DISABLED)
    default()

def buttons(x, img):
    imageSwap(img)
    textBox(x)
def interact(x):
    textBox(x)
    yesButton.pack_forget()
    noButton.pack_forget()
    northButton.pack_forget()
    eastButton.pack_forget()
    southButton.pack_forget()
    westButton.pack_forget()
    interactButton.pack_forget()
    attackButton.pack_forget()
    invButton.pack_forget()
    talkButton.pack(side=LEFT, padx=(182,5), pady=(0,15))
    takeButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    useButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    leaveButton.pack(side=LEFT, padx=(0,5), pady=(0,15))
    root.bind('<w>', lambda event:cant())
    root.bind('<a>', lambda event:talking(lib.current_room))
    root.bind('<s>', lambda event:buttons(pickup_items(lib.current_inventory), lib.rooms[lib.current_room]["image"]))
    root.bind('<d>', lambda event:buttons(use(lib.current_inventory), lib.rooms[lib.current_room]["image"]))
    root.bind('<e>', lambda event:default())
    root.bind('<r>', lambda event:cant())
    root.bind('<f>', lambda event:cant())
    root.bind('<q>', lambda event:cant())
def end_credits():
    yesButton.pack_forget()
    noButton.pack_forget()
    northButton.pack_forget()
    eastButton.pack_forget()
    southButton.pack_forget()
    westButton.pack_forget()
    interactButton.pack_forget()
    attackButton.pack_forget()
    invButton.pack_forget()
    root.bind('<w>', lambda event:cant())
    root.bind('<a>', lambda event:cant())
    root.bind('<s>', lambda event:cant())
    root.bind('<d>', lambda event:cant())
    root.bind('<e>', lambda event:cant())
    root.bind('<r>', lambda event:cant())
    root.bind('<f>', lambda event:cant())
    root.bind('<q>', lambda event:cant())
def cant():
    return

def GUICreation():
    #creating the UI for the program to run
    global root,titleCanvas,titleImage,titleCanvas,dispBG,displayFrame,subCanvas,dfbg,subCanvas,img,displayCanvas
    global textLogFrame,textCanvas,tbbg,textBG,actionsFrame,actionsCanvas,abg,actionsBG,textLog,scrollbar
    root = Tk() #Establishing the root window.
    root.iconbitmap("files\\images\\icon.ico") #importing our icon for the game.
    root.title("Adventure Cave") #The text that displays in the window's top bar.
    root.geometry("700x400+600+200") #setting the size of the screen for our game as well as where the window opens.
    root.resizable(0,0) #disabling resizing of the window.
    titleCanvas = Canvas(root, width=700, height=400, bd=0, highlightthickness=0)
    titleImage = ImageTk.PhotoImage(Image.open("files\\images\\titleScreen.png"))
    titleCanvas.background = titleImage
    dispBG = titleCanvas.create_image(0, 0, anchor=NW, image=titleImage)
    titleCanvas.pack_propagate(False)
    #creating the frame that will hold the image display label.
    displayFrame = Frame(root, bg='red', width=700, height=260, bd=0) 
    #creating a subCanvas so we can use an image as the UI background.
    subCanvas = Canvas(displayFrame, width=700, height=260, bd=0, highlightthickness=0)
    dfbg = ImageTk.PhotoImage(Image.open("files\\images\\displayFrameBG.png"))
    subCanvas.background = dfbg
    dispBG = subCanvas.create_image(0, 0, anchor=NW, image=dfbg)
    subCanvas.pack_propagate(False)
    #Importing our display image and attaching display to the sub canvas.
    img = ImageTk.PhotoImage(Image.open("files\\images\\C2.png"))
    displayCanvas = Label(subCanvas, image=img, width=500, height=260, bd=0)
    #creating the frame that will hold the text log, packing the text log frame, making the text log frame static, making the text canvas static and importing the UI bg.
    textLogFrame = Frame(root, bg='blue', width=700, height=90, bd=0) 
    textLogFrame.pack_propagate(False)
    textCanvas = Canvas(textLogFrame, width=700, height=90, bd=0, highlightthickness=0)
    textCanvas.pack_propagate(False)
    tbbg = ImageTk.PhotoImage(Image.open("files\\images\\textFrameBG.png"))
    textCanvas.background = tbbg
    textBG = textCanvas.create_image(0, 0, anchor=NW, image=tbbg)
    #creating the frame that will hold the action buttons, packing the actions frame, making the actions frame static, making the actions canvas static and importing the UI bg.
    actionsFrame = Frame(root, bg='green', width=700, height=50, bd=0) #establishing the frame that holds the action bar.
    #packing the action bar frame.
    actionsFrame.pack_propagate(False) #making the action bar frame static.
    actionsCanvas = Canvas(actionsFrame, width=700, height=50, bd=0, highlightthickness=0)
    actionsCanvas.pack_propagate(False)
    abg = ImageTk.PhotoImage(Image.open("files\\images\\actionsFrameBG.png"))
    actionsCanvas.background = abg
    actionsBG = actionsCanvas.create_image(0, 0, anchor=NW, image=abg)
    #setting up the text widget and packing it to the canvas.
    textLog = Text(textCanvas, wrap=WORD, font='Helvetica, 10', width=69, height=90, fg='white', bg='black', bd=0) #establishing the text log.
    #setting, packing and configuring the scrollbar to the text frame.
    scrollbar = Scrollbar(textCanvas, width=0, bd=0)
    textLog.config(yscrollcommand=scrollbar.set)
    #making a tag for text that is inputted to be centered on screen.
    textLog.tag_configure('center', justify='center')
    #actually configuring the scrollbar command to vertically scroll the text box.
    scrollbar.config(command=textLog.yview)

def settingsButtons():
    #setting up buttons
    global newGameButton,quitButton,quitButtonTitle,northButton,eastButton,southButton,westButton
    global interactButton,attackButton,takeButton,invButton,yesButton,noButton,talkButton,useButton,leaveButton
    newGameButton = Button(titleCanvas, text='Start Game', fg='white', bg='brown', width=10, command=lambda:intro())
    quitButton = Button(subCanvas, text='Quit', fg='white', bg='brown', width=10, command=root.quit)
    quitButtonTitle = Button(titleCanvas, text='Quit', fg='white', bg='brown', width=10, command=root.quit)
    northButton = Button(actionsCanvas, text='North (W)', fg='white', bg='brown', width=10, command=lambda:buttons(move_room("North"),lib.rooms[lib.current_room]["image"]))
    eastButton = Button(actionsCanvas, text='East (D)', fg='white', bg='brown', width=10, command=lambda:buttons(move_room("East"),lib.rooms[lib.current_room]["image"]))
    southButton = Button(actionsCanvas, text = 'South (S)', fg='white', bg='brown', width=10, command=lambda:buttons(move_room("South"),lib.rooms[lib.current_room]["image"]))
    westButton = Button(actionsCanvas, text='West (A)', fg='white', bg='brown', width=10, command=lambda:buttons(move_room("West"),lib.rooms[lib.current_room]["image"]))
    interactButton = Button(actionsCanvas, text='Interact (E)', fg='white', bg='brown', width=10, command=lambda:interact(lib.interaction))
    attackButton = Button(actionsCanvas, text='Attack (R)', fg='white', bg='brown', width=10, command=lambda:attack(lib.current_room,lib.current_inventory))
    takeButton = Button(actionsCanvas, text='Take (S)', fg='white', bg='brown', width=10, command=lambda:buttons(pickup_items(lib.current_inventory), lib.rooms[lib.current_room]["image"]))
    invButton = Button(actionsCanvas, text='Inventory (Q)', fg='white', bg='brown', width=10, command=lambda:buttons(lib.current_inventory, lib.rooms[lib.current_room]["image"]))
    yesButton = Button(actionsCanvas, text='Yes (A)', fg='white', bg='brown', width=10, command=lambda:groblinisms(lib.talk_DZNTS,"Yes"))
    noButton = Button(actionsCanvas, text='No (S)', fg='white', bg='brown', width=10, command=lambda:groblinisms(lib.talk_DZNTS,"No"))
    talkButton = Button(actionsCanvas, text='Talk (A)', fg='white', bg='brown', width=10, command=lambda:talking(lib.current_room))
    useButton = Button(actionsCanvas, text='Use (D)', fg='white', bg='brown', width=10, command=lambda:buttons(use(lib.current_inventory), lib.rooms[lib.current_room]["image"]))
    leaveButton = Button(actionsCanvas, text='Leave (E)', fg='white', bg='brown', width=10, command=lambda:default())