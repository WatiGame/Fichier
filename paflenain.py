import pygame
from pygame.locals import *
from Functions import *
from const import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

#Icone
#icone = pygame.image.load(image_icone)
#pygame.display.set_icon(icone)

#Titre
pygame.display.set_caption(title_screen)


#BOUCLE PRINCIPALE
continuer = 1
while continuer:    
    #Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))

    #Rafraichissement
    pygame.display.flip()

    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:
    
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():
        
            #Si l'utilisateur quitte, on met les variables 
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                #Variable de choix du niveau
                choix = 0
                
            elif event.type == KEYDOWN:             
                #Lancement du jeu
                if event.key == K_RETURN:
                    continuer_accueil = 0   #On quitte l'accueil
                    choix = 'start'        #On définit le niveau à charger
    
    #on vérifie que le joueur a bien fait un choix de niveau
    #pour ne pas charger s'il quitte
    if choix != 0:
        #Chargement du fond
        fond = pygame.image.load(image_fond).convert()

        #Génération d'un niveau à partir d'un fichier
        niveau = Start(choix)
        niveau.generer()
        niveau.afficher(fenetre)

        #Création de Donkey Kong
        dk = Perso("images/dk_droite.png", "images/dk_gauche.png", 
        "images/dk_haut.png", "images/dk_bas.png", niveau)

                

        
