#Room images go here

A3image="A3.png"
A3imageb="A3-no-sword.png"
B3image="B3.png"
C0image="C0.png"
C1image="C1.png"
C2image="C2.png"
C2imageb="C2-no-rocks.png"
C3image="C3.png"
C4image="C4.png"
DZNTSimage="DZNTS.png"
BA2image="BA2.png"
BA2imageb="BA2-dead-orc.png"
BA2imagec="BA2-no-ruby.png"
BB0image="BB0.png"
BB1image="BB1.png"
BB1imageb="BB1-no-slime.png"
BB2image="BB2.png"
BC0image="BC0.png"
B0BAimage="B0BA.png"
B0BAimageb="B0BA-egg.png"
BD0image="BD0.png"
#Room descriptions go here
A3 = "The room is dark.  A faint glow shines from the blade wedged in a thick stone in the center of the room.  The walls dance in the dim light as if telling a tale of the blades past.  The wars it fought.  The men it wielded.  A story unfolds in your brain in almost immaculate detail before returning once more to the smooth, almost featureless cavern you were in before.  The way back is to the south."
A3b= "The room is dark.  A smooth, almost featureless cavern.  An empty hole lies in a stone to the center of the room.  There is no magic here.  The way back is to the south."
B3 = "You stand upon a narrow path, to either side a sheer drop into the abyss.  You can barely make out the ground below, maybe there is a way down there?  To the north is a door-shaped passage, to the south is a four way junction."#Chasm Room with bridge
C0 = "Code by Kaden de Frece and Ryan McGrandle\nStory by Kaden de Frece and Ryan McGrandle\nArt by Ryan McGrandle\nOriginal Theme by Lydia Kneiss\nThank you so much for playing!"#Exit/Escape
C1 = "The pathway is lit up by the warmth of sunlight.  You breath in the sharp, crisp air.  It feels like a mother's hug.  The way forward is to the west.  The way back is to the east."#Caved in room, need pickaxe to break into this room
C2 = "A cave in lays before you.  Rocks upon rocks are piled up and block the path to the west.  To the east is a four way junction."#Start Room
C2b= "The way is clear, all you have to do is take that next step.  You can see the faint light of day creeping in far down the path to the west.  To the east is a four way junction."
C3 = "You are in the center of a four way junction.  The cave walls are smooth and reflect the light of a single torch, its flames flickering and dancing in the still air.  To the north is a narrow natural bridge.  To the west is the room where the cave-in happened.  To the south is a door-way, a faint ringing of metal can be heard from within.  To the east is a stairwell leading further down into the cave."#Intersection Room Can go any direction
C4 = "A stairwell spirals down into the void deep below.  Using the stairwell will lead you deeper.  The way back is to the west."#Stairwell Room
DZNTS = "A small green goblin sits behind an anvil.  He takes a break from his work after noticing you enter.  Upon the anvil rests a pickaxe.  The room is otherwise decorated with various trinkets and tools that you assume belong to this goblin.  The way back is to the north."#Groblin's Smithy
DZNTSb= "Groblin the goblin sits behind his anvil.  He takes a break from his work after noticing you enter.  Upon the anvil rests a pickaxe.  The room is otherwise decorated with various trinkets and tools that you assume belong to him.  The way back is to the north."
DZNTSc= "Groblin the goblin sits behind his anvil.  He takes a break from his work after noticing you enter.  Upon the anvil  there is a small ring, Groblin appears to be fashioning the ruby into something new.  The room is otherwise decorated with various trinkets and tools that you assume belong to him.  The way back is to the north."
BA2 = "A large orc stands with his back to you.  He appears to be working on something, though you can't make out what.  He doesn't seem to notice you.  The way back is to the south."#Jacu's Office
BA2b= "A ruby sits atop a blood soaked work table suspended by chains.  On the ground lies a sight not appropriate for our target ESRB rating. The way back is to the south."
BA2c= "An empty blood soaked work table suspended by chains rests against the wall in front of you.  On the ground lies a sight not appropriate for our target ESRB rating.  The way back is to the south."
BB0 = "The hallway curves to the east.  The walls are dark and featureless.  To the south, the hallway continues with a break in the wall for a staircase leading back up the cave."#Corner Room East to Slime, South to Stairwell
BB1 = "An orange slime gyrates before you.  It is goopy, and quite gross.  Bits of bone float in its translucent body.  the way back is to the west."#Stephan the Slime Hallway
BB1b="The hallway is empty.  The way forward is to the east.  the way back is to the west."
BB2 = "The hallway comes to a stop.  However there is a lit doorway to the north and a pitch eerie blackness to the south.  The way back is west."#T intersection room, North To Jacu, South to Boba
BC0 = "You are standing at the foot of a long, winding staircase.  The hallway it stops in abruptly runs to the north and south.  Using the stairwell will bring you back up."#Stairwell Room
B0BA = "The room is as dark as the void of space.  A creature lounges lazily, staring at you.  Into you.  Beyond you?  Actually, you can't quite tell what the creature is looking at.  It begins to sniff the air around you, its tail flicking in the soft light from behind you."#Boba Demon room
BD0 = "The room is pitch black.  You can barely feel around.  The way back is to the north."#BD0 Darkness Room, Need Ruby for light
#Dialogue options
dialogue ={
    "goblin_dialogue_1":
        {
        "Talk":"The goblin raises his gaze to meet yours.  \"Hello traveller my name is Groblin.  I see you want my pickaxe.  I will give it to you.  However, this pickaxe is dear to me. If you want it, I need something from you.  Jacu the Orc stole my precious ruby.  Would you recover it for me?  He lives deep within the cave below.  But beware, there are many other dangers deep within the cave besides just him.\"",
        "Talk_b":"The goblin raises his gaze to meet yours.  \"Hello again traveller.  Have you reconsidered my offer?  Jacu still lays deep within the cave with my precious ruby.\""
        },
    "goblin_dialogue_2":
        {
        "No":"\"Understandable, have a great day.\"",
        "Yes":"\"Excellent!  Thank you!  Please take this rope, I hope it will aid you in your journey.\""  
        },
    "goblin_dialogue_3":
        {
        "Talk":"\"Gasp I-is that my ruby?  Please!  You must give it to me!\"",
        "Talk_b":"\"Please!  You must give me the Ruby!\""    
        },
    "goblin_dialogue_4":
        {
        "Yes":"\"Thank you hero!  Please take my pickaxe.  May it serve you well.\"",
        "No":"\"Please reconsider.  I need that ruby, it's everything to me.\""
        },
    "goblin_dialogue_5":"\"Oh!  I just thought of something.  Would you hear me out, young Hero?\"",
    "goblin_dialogue_6":"Groblin continues to rant about any little thing that crosses his mind.  Unfortunately, you've heard it all and are now just wasting your time.  Good on you for keeping this small green man company for so long.",
    "goblin_attack":
        {
        "Fist":"You lash out at the goblin with your fists The goblin speaks \"You could at least hear my story first...\"",
        "Caliboard":"You strike at the mind goblin! You feel your sword tear through his flesh... You blink and suddenly find yourself staring at the unharmed goblin a few feet ahead of you, he is giving you an annoyed look. Maybe thats not such a good idea...",
        },
    "orc_attack":"You strike fast and hard.  Faster than the orc can react!  In one fell swoop, you cleave the orc in two.  Showering the room with blood and gore.  You see now what the orc was working on, a small ruby glints under all the blood.",
    "orc_talk":"The orc turns quickly after the first noise leaves your mouth.  Then you hear a deafening thud as your vision goes red.",
    "slime_attack":"You strike the slime as hard as you can.  Bits of icky stuff go flying and the slime is defeated! Something mysterious is left behind!",
    "B0BA_talk":
        {
        "Talk":"The creature sniffs at your pocket, it seems to want the slime egg you picked up.  Give it the slime egg?",
        "Yes":"The creature smacks the slime egg onto the ground with a wet thud.  She looks satisfied.  You also found a grape on the ground! You promptly exit before the creature turns its attention back to you.",
        "No":"The creature pounces to grab the egg, knocking you down.  The egg falls from your pocket and in the confusion, you black out."  
        },
    "B0BA_attack":"Before you could even think about it, you feel an unbearable pain!",
    "weaponless":"Without a weapon your attack is useless against the enemy"
}
#Initializing Variables
START_ROOM = 'C2' #room player starts in
current_room = START_ROOM #intializing the current room for movement
no_grapes = 0 #minimum number of grapes
max_grapes = 4 #maximum number of grapes a player can have
current_inventory = ["Inventory:"] #starting the player with nothing
direction = '' #Default direction is None
#initializing quests
slime_dead = False
orc_dead = False
pickaxe = False
wall_break = False
caliboard = True
#initializing grape counter, increments by 1 for every grape obtained
grape_count = 0 
#managing goblin conversations
goblin_chat_counter = 0
#This is used to send the player out of the talk screen when they cause an action with their yes/no buttons
interaction = print("",end="")
#this is used as a reference so players can't obtain the same grape twice, they are removed upon incrementing grape counter 
grapes = [ #Grape 1 ="DZNTS", Grape 2 ="B3", Grape 3="B0BA", Grape 4="BD0"
            "Grape 1","Grape 2","Grape 3","Grape 4"]
talk_DZNTS = ["Did I ever tell you about the time I got lost in a cave?...",
                "Did I ever tell you about the time I got lost in a cavern?...",
                "Did I ever tell you about myself?...",
                "Have you ever been in a Turkish prison?",
                "Y'know, I used to have a kingdom of my own.  Yup.  The great Mind Goblin Aristocracy was a direct line to yours truly!  Unfortunately, I ran that country into the ground.  Bad times, got chased out, exiled, they even have a holiday named after that day.",
                "Woof, you reek.  Have you had a shower lately?",
                "I wrote a poem:  There once was a goblin from...",
             ]
#thes are the the strings printed if the player cannot pick up an item due to an incomplete quest
incomplete ={"BB1":"Is that an egg floating inside of the slime?  You'll have to kill it first if you want that.",
             "BA2":"There's something back there.  If only you had a way to dispose of Jacu.",
             "DZNTS":"The pickaxe is firmly within the Goblin's grasp!"}
rooms = {
        "A3": {"name": A3, "South": "B3","quest":caliboard,"item":"Caliboard","image":A3image},
        "B3": {"name": B3, "North": "A3", "South": "C3","image":B3image},
        "C0": {"name": C0, "East": "C1","image":C0image},
        "C1": {"name": C1, "East": "C2", "West": "C0","image":C1image},
        "C2": {"name": C2, "East": "C3","image":C2image},
        "C3": {"name": C3, "North": "B3", "East": "C4", "South": "DZNTS", "West": "C2","image":C3image},
        "C4": {"name":C4, "West": "C3","image":C4image},
        "DZNTS": {"name": DZNTS, "North": "C3","quest":pickaxe,"item":"Pickaxe","image":DZNTSimage},
        "BA2": {"name": BA2, "South": "BB2","quest":orc_dead,"item":"Ruby","image":BA2image},
        "BB0": {"name": BB0, "East": "BB1", "South": "BC0","image":BB0image},
        "BB1": {"name": BB1, "West": "BB0","quest":slime_dead,"item":"Slime Egg","image":BB1image},
        "BB2": {"name": BB2, "North": "BA2", "South": "B0BA", "West": "BB1","image":BB2image},
        "BC0": {"name": BC0, "North": "BB0", "South": "BD0","image":BC0image},
        "B0BA": {"name": B0BA, "North": "BB2","image":B0BAimage},
        "BD0": {"name": BD0, "North": "BC0","image":BD0image}
        }