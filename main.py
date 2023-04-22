from pygame import mixer #Importing the pygame library.  If not working install by typing 'pip install pygame' into your terminal (ctrl+shift+` in VSC).
import random #importing the random library
import files.data.functions as fn #importing our functions.py
import files.data.library as lib #importing our library.py
mixer.init() #initializing the pygame mixer
fn.GUICreation()
#loading and playing the soundtrack, credit to the artist Lydia Kneiss for making this original score.
mixer.music.load("files\\sounds\\Adventure Cave - Main Theme.mp3") 
fn.settingsButtons()

if __name__ == "__main__":
    mixer.music.play(-1)
    random.shuffle(lib.talk_DZNTS)
    fn.titleScreen()
    fn.root.mainloop() #setting the end of the GUI mainloop.