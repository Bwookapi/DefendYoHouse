"""
This Game will simulate an invasion of zombies 
"""

import pgzrun
import random
import os
import pygame
import time

#***GAME ENVIRONMENT SETTING*******************************************************************

os.environ['SDL_VIDEO_CENTERED'] = '1'

TITLE = 'Defend Yo House!!'

#SCREEN SIZE 
HEIGHT = 675
WIDTH = 1200

#**********************************************************************************************

#***GLOBAL VARIABLES*************************************************************

Bobbk = Actor("bobback")
GameBackground = Actor("grass")
Fence = Actor("fence")
Fence2 = Actor("fence copy")
House = Actor("house")
Goku = Actor("gokubob")
Endgameblood = Actor("endgameblood")
Househealthbar = Actor ("5hp")
PlayerHealthBar = Actor ("maxpp")


ZombiesGroup1 = []
ZombiesGroup2 = []
ZombiesGroup3 = []
HouseList = []

Magic = []
Magic2 = []
Magic3 = []
Magic4 = []

HouseHealth = 5
PlayerHealth =3
Score = 0

#Game states 

# 0 -- > Menu 
# 1 -- > In Game
# 2 -- > Game Over 
GameState = 0

#********************************************************************************

#***FUNCTIONS**********************************************************************************


    


def MenuScreen():
    GameBackground.draw()
    House.draw()
    House.x = 1000
    Goku.draw()
    Goku.x = 750
    Goku.y = 485
    screen.draw.text(str("DEFEND YOUR HOUSE!!"), (100, 100), fontname="lol", fontsize = 50, color = 'darkgreen')
    screen.draw.text(str("Press 1 to Start"), (150, 250), fontname="lol", fontsize = 36, color = 'darkgreen')
    screen.draw.text(str("Press 2 to Quit"), (150, 350), fontname="lol", fontsize = 36, color  = 'darkgreen') #No thank you manav g! ;)
    screen.draw.text(str("Press 3 to see Instructions"), (150, 450), fontname="lol", fontsize = 36, color   = 'darkgreen') #No thank you manav g! ;)

def Instructions():
    GameBackground.draw()
    screen.draw.text("Welcome to 'Defend Yo House!'", (330, 40), fontname="lol", fontsize=50, color="red")

    screen.draw.text("A game where all hopes for humanity are lost,", (370, 90), fontname="lol", fontsize=28, color="black")
    screen.draw.text("but our main character Bob still perseveres through the Zombie Apocalypse.", (150, 125), fontname="lol", fontsize=28, color="black")

    screen.draw.text("Objective:", (530, 180), fontname="lol", fontsize=36, color="red")
    screen.draw.text("Stay alive and prevent your house from getting destroyed by zombies!", (140, 215), fontname="lol", fontsize=28, color="black")

    screen.draw.text("Zombies come from all sides.", (450, 255), fontname="lol", fontsize=28, color="black")
    screen.draw.text("Use your spells to cast them down,", (430, 290), fontname="lol", fontsize=28, color="black")
    screen.draw.text("which you learned from a clickbait YouTube video.", (280, 325), fontname="lol", fontsize=28, color="black")

    screen.draw.text("You have 3 lives and your house tanks 5 hits. If one runs out, YOU DIE.", (150, 360), fontname="lol", fontsize=28, color="black")

    screen.draw.text("Controls:", (530, 400), fontname="lol", fontsize=36, color="red")
    screen.draw.text("- Use 'W A S D' to move  (W = Up   S = Down   A = Left   D = Right)", (150, 435), fontname="lol", fontsize=28, color="black")
    screen.draw.text("- Press Arrow Keys to shoot spells.", (415, 470), fontname="lol", fontsize=28, color="black")
    screen.draw.text("- Also, zombies get faster each respawn!", (415, 505), fontname="lol", fontsize=28, color="black")


    screen.draw.text("Press 1 to go back to Menu", (440, 560), fontname="lol", fontsize=30, color="black")



def GameOver():
    Endgameblood.draw()
    screen.draw.text(str("YOU DIED"), (100, 70), fontname="lol", fontsize = 65, color = 'black')
    screen.draw.text(str("Press 1 to restart"), (450, 85), fontname="lol", fontsize = 26, color = 'black')
    screen.draw.text(str("Press 2 to quit"), (700, 85), fontname="lol", fontsize = 26, color = 'black') #No thank you manav g! ;)
    screen.draw.text(str("Press 3 for Menu"), (950, 85), fontname="lol", fontsize = 26, color = 'black') #No thank you manav g! ;)

    Bobded = Actor("bobded")
    Bobded.x = Bobbk.x 
    Bobded.y = Bobbk.y   
    Bobded.draw()


def on_key_down(key):
    global GameState

    if GameState == 0:
        #accepted down keys while in the Menu
        if key == keys.K_1:
            #code to start to a game 

            InitGame()
        
        if key == keys.K_2:
            quit()

        if key == keys.K_3:
            #Instructions for game 
            GameState =3
            Instructions()


    if GameState ==1: 
        if key == keys.UP:
            Spell = Actor('blueball')
            Spell.x = Bobbk.x
            Spell.y = Bobbk.y - 45
            Magic.append(Spell)
        if key == keys.DOWN:
            Spell2 = Actor('blueball2')
            Spell2.x = Bobbk.x
            Spell2.y = Bobbk.y +45
            Magic2.append(Spell2)
        if key == keys.LEFT:
            Spell3 = Actor('blueball3')
            Spell3.x = Bobbk.x -45
            Spell3.y = Bobbk.y 
            Magic3.append(Spell3)
        if key == keys.RIGHT:
            Spell4 = Actor('blueball4')
            Spell4.x = Bobbk.x +45
            Spell4.y = Bobbk.y 
            Magic4.append(Spell4)

    elif GameState == 2:
        if key == keys.K_1:
            #code to start to a game 

            InitGame()
        
        if key == keys.K_2:
            quit()

        if key == keys.K_3:
            GameState = 0       

    elif GameState == 3:
        if key == keys.K_1:
            #starts the game from instruction screen
            GameState = 0 


def InitGame():
    global GameState
    global Bobbk
    global Fence2
    global Fence
    global House
    global ZombiesGroup1
    global Zombie1
    global ZombiesGroup2
    global Zombie2
    global ZombiesGroup3
    global Zombie3 
    global HouseHealth
    global Magic
    global Magic2
    global Magic3
    global Magic4
    global Spell
    global Spell2
    global Spell3
    global Spell4 
    global PlayerHealth

    Magic = []
    Magic2 = []
    Magic3 =[]
    Magic4 = []




  
#Character starting postion
    Bobbk.x= WIDTH//2 
    Bobbk.y= 350

#Fence starting position
    Fence.y = 500
    Fence.x = -50
    Fence2.y = 500
    Fence2.x = 1250

    House.x = WIDTH//2
    House.y = 0

    Househealthbar.y = 30
    Househealthbar.x = 150

    PlayerHealthBar.y = 30
    PlayerHealthBar.x = 1000




    #Setup zombies coming from bottom
    ZombiesGroup1 = []
    for i in range (5):
            Zombie1 = Actor('zombie1')
            Zombie1.y = random.randint (600,900)
            Zombie1.x = random.randint (200, 1000)
            Zombie1.speed = -0.5
            Zombie1.point = 3
            ZombiesGroup1.append(Zombie1)
            
    ZombiesGroup2 = []
    for i in range (2):
            Zombie2 = Actor('zombie2')
            Zombie2.y = random.randint (50,300)
            Zombie2.x = random.randint (1210, 1240)
            Zombie2.speed = -0.5
            Zombie2.point = 3
            ZombiesGroup2.append(Zombie2)

    
    ZombiesGroup3 = []
    for i in range (2):
            Zombie3 = Actor('zombie3')
            Zombie3.y = random.randint (50,300)
            Zombie3.x = random.randint (-30,-10)
            Zombie3.speed = 0.5
            Zombie3.point = 3
            ZombiesGroup3.append(Zombie3)
    
    GameState = 1
            
#**********************************************************************************************

#***GAME FUNCTIONS*****************************************************************************

def update():
    global GameState
    global Bobbk
    global Fence2
    global Fence
    global House
    global ZombiesGroup1
    global Zombie1
    global ZombiesGroup2
    global Zombie2
    global ZombiesGroup3
    global Zombie3 
    global HouseHealth
    global Magic
    global Magic2
    global Magic3
    global Magic4
    global Spell
    global Spell2
    global Spell3
    global Spell4
    global PlayerHealth
    global Score


    if GameState == 1:

        #in Game play mode 
        PrevX = Bobbk.x
        PrevY = Bobbk.y

    
    #left and right keys

        if keyboard.d:
            Bobbk.image = ("bobright")
            Bobbk.x = Bobbk.x + 6.5
        if keyboard.a:
            Bobbk.image = ("bobleft")
            Bobbk.x = Bobbk.x - 6.5


    #Up and down keys      
        if keyboard.w:
            Bobbk.y = Bobbk.y - 6.5
            Bobbk.image = ("bobback")
        if keyboard.s:
            Bobbk.y = Bobbk.y + 6.5
            Bobbk.image = ("bobfr")
        

        if Bobbk.colliderect(Fence2) or Bobbk.colliderect(Fence):
            Bobbk.x = PrevX
            Bobbk.y = PrevY
        
        if Bobbk.x == 0  or Bobbk.x == 1190:
            Bobbk.x = PrevX
            Bobbk.y = PrevY

        if Bobbk.y == 0  or Bobbk.y == 670:
            Bobbk.x = PrevX
            Bobbk.y = PrevY

        if Bobbk.colliderect(House):
            Bobbk.x = PrevX
            Bobbk.y = PrevY
        

        # Move all the spells
        for Spell in Magic[:]:
            if Spell.y <= -5:
                if Spell in Magic:  # Ensure the spell is in the list before removing
                    Magic.remove(Spell)
            else:
                Spell.y -= 5

        for Spell2 in Magic2[:]:
            if Spell2.y <= 5:
                if Spell2 in Magic2:
                    Magic2.remove(Spell2)
            else:
                Spell2.y += 5

        for Spell3 in Magic3[:]:
            if Spell3.x <= -5:
                if Spell3 in Magic3:
                    Magic3.remove(Spell3)
            else:
                Spell3.x -= 5

        for Spell4 in Magic4[:]:
            if Spell4.x <= 5:
                if Spell4 in Magic4:
                    Magic4.remove(Spell4)
            else:
                Spell4.x += 5
       
            
     


        #check if a bullet colides with an enemy 
        for Spell in Magic:
            for Zombie1 in ZombiesGroup1:
                if Zombie1.colliderect(Spell):
                    #a collision so remove the enemy and bullet

                    Zombie1.y = random.randint (750,950)
                    Zombie1.x = random.randint (300, 900)
                    Zombie1.speed += -0.05
                    Magic.remove(Spell)
                    Score += 1
                    break
               
            for Zombie2 in ZombiesGroup2:     
                if Zombie2.colliderect(Spell):
                    #a collision so remove the enemy and bullet

                    Zombie2.y = random.randint (50,300)
                    Zombie2.x = random.randint (1250, 1270)
                    Zombie2.speed += -0.05
                    Magic.remove(Spell)
                    Score += 1
                    break

            for Zombie3 in ZombiesGroup3:     
                if Zombie3.colliderect(Spell):
                    #a collision so remove the enemy and bullets

                    Zombie3.y = random.randint (50,300)
                    Zombie3.x = random.randint (-70, -50)
                    Zombie3.speed += 0.05
                    Magic.remove(Spell)
                    Score += 1
                    break
        
        for Spell2 in Magic2:
            for Zombie1 in ZombiesGroup1:               
                if Zombie1.colliderect(Spell2):
                    #a collision so remove the enemy and bullet

                    Zombie1.y = random.randint (750,950)
                    Zombie1.x = random.randint (300, 900)
                    Zombie1.speed += -0.05
                    Magic2.remove(Spell2)
                    Score += 1
                    break
            
            for Zombie2 in ZombiesGroup2:     
                if Zombie2.colliderect(Spell2):
                    #a collision so remove the enemy and bullet

                    Zombie2.y = random.randint (50,300)
                    Zombie2.x = random.randint (1250, 1270)
                    Zombie2.speed += -0.05
                    Magic2.remove(Spell2)
                    Score += 1
                    break

            for Zombie3 in ZombiesGroup3:     
                if Zombie3.colliderect(Spell2):
                    #a collision so remove the enemy and bullet

                    Zombie3.y = random.randint (50,300)
                    Zombie3.x = random.randint (-70, -50)
                    Zombie3.speed += 0.05
                    Magic2.remove(Spell2)
                    Score += 1
                    break
        
        for Spell3 in Magic3:
            for Zombie1 in ZombiesGroup1:               
                if Zombie1.colliderect(Spell3):
                    #a collision so remove the enemy and bullet

                    Zombie1.y = random.randint (750,950)
                    Zombie1.x = random.randint (300, 900)
                    Zombie1.speed += -0.05
                    Magic3.remove(Spell3)
                    Score += 1
                    break
                
            for Zombie2 in ZombiesGroup2:     
                if Zombie2.colliderect(Spell3):
                    #a collision so remove the enemy and bullet

                    Zombie2.y = random.randint (50,300)
                    Zombie2.x = random.randint (1250, 1270)
                    Zombie2.speed += -0.05
                    Magic3.remove(Spell3)
                    Score += 1
                    break

            for Zombie3 in ZombiesGroup3:     
                if Zombie3.colliderect(Spell3):
                    #a collision so remove the enemy and bullet

                    Zombie3.y = random.randint (50,300)
                    Zombie3.x = random.randint (-70, -50)
                    Zombie3.speed += 0.05
                    Magic3.remove(Spell3)
                    Score += 1
                    break

        for Spell4 in Magic4:
            for Zombie1 in ZombiesGroup1:          
                if Zombie1.colliderect(Spell4):
                    #a collision so remove the enemy and bullet
                    Magic4.remove(Spell4)
                    Zombie1.y = random.randint (750,950)
                    Zombie1.x = random.randint (300, 900)
                    Zombie1.speed += -0.05
                    Score += 1
                    break
            
            for Zombie2 in ZombiesGroup2:     
                if Zombie2.colliderect(Spell4):
                    #a collision so remove the enemy and bullet
                    Magic4.remove(Spell4)
                    Zombie2.y = random.randint (50,300)
                    Zombie2.x = random.randint (1250, 1270)
                    Zombie2.speed += -0.05
                    Score += 1
                    break

            for Zombie3 in ZombiesGroup3:     
                if Zombie3.colliderect(Spell4):
                    #a collision so remove the enemy and bullet
                    Magic4.remove(Spell4)
                    Zombie3.y = random.randint (50,300)
                    Zombie3.x = random.randint (-70, -50)
                    Zombie3.speed += 0.05
                    Score += 1
                    break
 
        

        #move all the enemies
        for Zombie1 in ZombiesGroup1:
            Zombie1.y += Zombie1.speed
            #check if the enemy is beyond the bottom of the screen
            if Zombie1.y < -25 :
                #respawn enemy at the bottom of the screen

                Zombie1.y = random.randint (750,950)
                Zombie1.x = random.randint (300, 900)
                Zombie1.speed += -0.05

            if Zombie1.colliderect(House):
                HouseHealth -= 1
                if HouseHealth == 4:
                    Househealthbar.image = ("4hp")

                if HouseHealth == 3:
                    Househealthbar.image = ("3hp")

                if HouseHealth == 2:
                    Househealthbar.image = ("2hp")

                if HouseHealth == 1:
                    Househealthbar.image = ("1hp")

                if HouseHealth == 0:
                    PlayerHealthBar.image = ("maxpp")
                    Househealthbar.image = ("5hp")
                    GameState = 2
                    HouseHealth = 5
                    PlayerHealth = 3
                    Score = 0 

               
                Zombie1.y = random.randint (750,950)
                Zombie1.x = random.randint (300, 900)


            if Zombie1.colliderect(Bobbk):
                PlayerHealth -= 1
                Zombie1.y = random.randint (750,950)
                Zombie1.x = random.randint (300, 900)
                
                if PlayerHealth == 2:
                    PlayerHealthBar.image = "2pp"
                elif PlayerHealth == 1:
                    PlayerHealthBar.image = "1pp"
                elif PlayerHealth <= 0:
                    GameState = 2
                    HouseHealth = 5
                    PlayerHealth = 3
                    PlayerHealthBar.image = ("maxpp")
                    Househealthbar.image = ("5hp")   
                    Score = 0 
      
                
                Zombie1.y = -100
                    


        
        for Zombie2 in ZombiesGroup2:
            Zombie2.x += Zombie2.speed
            #check if the enemy is beyond the right of the screen
            if Zombie2.x < 30 :
                #respawn enemy at the right of the screen

                Zombie2.y = random.randint (50,300)
                Zombie2.x = random.randint (1210, 1240)
                Zombie2.speed += -0.05

            if Zombie2.colliderect(House):
                HouseHealth -= 1
                if HouseHealth == 4:
                    Househealthbar.image = ("4hp")

                if HouseHealth == 3:
                    Househealthbar.image = ("3hp")

                if HouseHealth == 2:
                     Househealthbar.image = ("2hp")

                if HouseHealth == 1:
                     Househealthbar.image = ("1hp")

                if HouseHealth == 0:
                    PlayerHealthBar.image = ("maxpp")
                    Househealthbar.image = ("5hp")
                    GameState = 2
                    HouseHealth = 5
                    PlayerHealth = 3    
                    Score = 0 
            
                
                Zombie2.y = random.randint (50,300)
                Zombie2.x = random.randint (1210, 1240)            
           
            if Zombie2.colliderect(Bobbk):
                PlayerHealth -= 1
                Zombie2.y = random.randint (50,300)
                Zombie2.x = random.randint (1210, 1240)

                if PlayerHealth == 2:
                    PlayerHealthBar.image = "2pp"
                elif PlayerHealth == 1:
                    PlayerHealthBar.image = "1pp"
                elif PlayerHealth <= 0:
                    Househealthbar.image = ("5hp")      
                    PlayerHealthBar.image = "maxpp"
                    GameState = 2
                    HouseHealth = 5
                    PlayerHealth = 3
                    Score = 0 


    

    


        for Zombie3 in ZombiesGroup3:
            Zombie3.x += Zombie3.speed
            #check if the enemy is beyond the left of the screen
            if Zombie3.x > 1230 :
                #respawn enemy at the left of the screen

                Zombie3.y = random.randint (50,300)
                Zombie3.x = random.randint (-30, -10)
                Zombie3.speed += 0.05

            if Zombie3.colliderect(House):
                HouseHealth -= 1
                if HouseHealth == 4:
                    Househealthbar.image = ("4hp")

                if HouseHealth == 3:
                    Househealthbar.image = ("3hp")

                if HouseHealth == 2:
                     Househealthbar.image = ("2hp")

                if HouseHealth == 1:
                     Househealthbar.image = ("1hp")

                if HouseHealth == 0:
                    PlayerHealthBar.image = "maxpp"
                    Househealthbar.image = ("5hp")
                    GameState = 2
                    HouseHealth = 5
                    PlayerHealth = 3
                    Score = 0 


                Zombie3.y = random.randint (50,300)
                Zombie3.x = random.randint (-30, -10)
            
            if Zombie3.colliderect(Bobbk):
                PlayerHealth -= 1

                Zombie3.y = random.randint (50,300)
                Zombie3.x = random.randint (-30, -10)

                if PlayerHealth == 2:
                    PlayerHealthBar.image = "2pp"
                elif PlayerHealth == 1:
                    PlayerHealthBar.image = "1pp"
                elif PlayerHealth <= 0:
                    Househealthbar.image = ("5hp")  
                    PlayerHealthBar.image = "maxpp"
                    GameState = 2
                    HouseHealth = 5
                    PlayerHealth = 3
                    Score = 0 


                Zombie3.x = -100           
            

    


# States of game (ex. menu, in game, death screen)
def draw():

    if GameState == 0:
        MenuScreen() 

        
    elif GameState == 1:   
        

        screen.clear()
        GameBackground.draw() 
        Fence.draw()
        Fence2.draw()
        Bobbk.draw()
        House.draw()
        for Zombie1 in ZombiesGroup1:
            Zombie1.draw()
        
        for Zombie2 in ZombiesGroup2:
            Zombie2.draw()

        for Zombie3 in ZombiesGroup3:
            Zombie3.draw()
        
        Househealthbar.draw()
        PlayerHealthBar.draw()

        for Spell in Magic:
            Spell.draw()

        for Spell2 in Magic2:
            Spell2.draw()

        for Spell3 in Magic3:
            Spell3.draw()

        for Spell4 in Magic4:
            Spell4.draw()

        
        screen.draw.text(str("House health bar"), (100, 45), fontname="lol", fontsize = 20, color = 'black')
        screen.draw.text("Score: " + str(Score),(1000, 620), fontname = "lol", fontsize =40, color="black")



    elif GameState == 2:
        GameOver()

    elif GameState == 3:
        Instructions()    

#**********************************************************************************************


pgzrun.go()