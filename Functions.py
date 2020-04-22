import pygame
from pygame.locals import *
from const import *

#AFFICHAGE MENU
#def Start(choix):
    #for event in pygame.event.get():
     #   if event.type==KEYDOWN:
      #      if event.key== K_RETURN:
       #         choix = 1           
    #si le joueur appuie sur la touche "Entrée", l'image start disparaît
    #et le chariot commence déjà à avancer (peut être ajouter avant
    # "Etes vous prêt ? " un truc comme ça

class Chariot:
    """Classe permettant de créer le chariot, caractérisé par :
        - sa position x et y
        - sa direction, toujours vers la droite ? (je sais pas si c'est important de le mentionner)
        - sa vitesse"""
    
    def __init__(self,x,y,vx,vy):
        #Sprites du personnage
        self.car = pygame.image.load(image_car).convert_alpha()
        self.car_penché = pygame.image.load(image_car_penché).convert_alpha()
        
        #position
        self.x = x
        self.y = y
        
        #vitesse
        self.vx = vx
        self.vy = vy
        
        #Direction par défaut
        self.direction = self.car
        
    def sautchariot :
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key== K_SPACE:
                    self.car.penché
                    self.y+=4
                    self.x+=3
    
               
class Nain:
    """Classe permettant de créer le nain, caractérisé par :
        - sa position x et y
        - sa trajectoire
        - son poids ? (selon le nain)
        - sa vitesse ?
        - sa direction (je ne sais pas si c'est aussi important de le signaler ?"""
    def __init__(self,nx,ny,vnx,vny,np,trn):
        #sprites du personnages
        #self.nain = pygame.image.load(image_nain).convert.
        
        #position
        self.nx = nx
        self.ny = ny
        
        #vitesse
        self.vnx = vnx
        self.vny = vny
        
        #son poids
        self.np = np
        
        #sa trajectoire
        self.trn = trn
        
    #def volnain (self):
        #ça serait pour la trajectoire
