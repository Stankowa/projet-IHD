import pygame

pygame.init()

# Définir les dimensions de la fenêtre
dimension = (800,600)
# Créer la fenêtre principale
fenetre = pygame.display.set_mode(dimension)

# Définir le titre de la fenêtre
pygame.display.set_caption("Ma première fenêtre Pygame")

#creer la surface secondaire
surface = None
font = pygame.font.SysFont("cambria",18)

def afficher(id):
    global surface, debut
    surface = pygame.Surface((250, 100))
    surface.fill((47, 174, 179))
    touche = pygame.key.name(id)
    texte_nom = font.render(f"La touche appuyer est : {touche}", True, (0, 0, 0))
    texte_id = font.render(f"Son ID est : {id}", True, (0, 0, 0))
    surface.blit(texte_nom, (10, 30))
    surface.blit(texte_id, (10, 50))
    debut = pygame.time.get_ticks()



#liste variables
    #parametre temps
temps_T = 2.5 * 1000
debut = 0
    #parametre touche
touche = None
    # Boucle principale du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # recuperer l'id de la touche appuye
        elif event.type == pygame.KEYDOWN:
            touche_id = event.key
            touche = pygame.key.name(touche_id)
            afficher(touche_id)


    # affichage conditionnel de la touche appuyer
    if surface is not None:
        temps_E = pygame.time.get_ticks() - debut
        if temps_T <= temps_E :
            surface = None

    fenetre.fill((126,246,251))
    font2 = pygame.font.SysFont("cambria", 30)
    font3 = pygame.font.SysFont("cambria", 15)
    intro = font2.render("Exemple de fonctionnement d'une IHD", True, (0, 0, 0))
    fenetre.blit(intro, (40, 10))
    instr = font3.render("Appuyer sur n'importe quel touche du clavier", True, (0, 0, 0))
    fenetre.blit(instr, (40, 100))
    if surface is not None:
        fenetre.blit(surface, (300,250))

    # actuallisation de la fenetre
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
