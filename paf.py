import pygame
from pygame.locals import *
from pygame import *
import time


pygame.init()
mixer.init()

#Initialization of variables 
x=0
y=-50

# display of all the images and the proprieties

        #car
car= pygame.image.load('chariot.png')
car2 = pygame.transform.scale(car,(250,250))

background = pygame.image.load('bg2.jpg')
background2 = pygame.transform.scale(background,(1678,1000))

#générer la fenêtre
pygame.display.set_caption("Paf le Dwarf") #nom de fenêtre
screen = pygame.display.set_mode ((1678,1000)) # premier : largeur / deuxième  : hauteur

#musique
music=mixer.Sound("music2.wav")
#boucle tant que running est vraie donc ça veut dire que tant que c'est vrai le fenêtre 
#reste ouverte
running = True
while running:
     music.play()
     screen.blit(background2,(0,0))     
#appliquer l'image du chariot + vitesse
     screen.blit(car2,(x,y))
     #update l'écran
     x =x+15
     y= 0
     if x>150:
          x=x+20
          y=0
     if x>300:
          x=x+30
          y=0
     pygame.display.flip()
     for event in pygame.event.get():
        # que l'évènement est fermeture de fenêtre
        if event.type == pygame.QUIT:
             running= False 
mixer.qui() 
pygame.quit()


 
