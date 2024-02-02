import pygame
import random
import numpy as np

SCREEN_COLOR = (50, 50, 50)
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 540
CLOCK_FREQUENCY = 5

TILES_SIZE = 18
TILES_COLOR = (15, 15, 15)

NUMBER_OF_TILES_HEIGHT = SCREEN_HEIGHT // TILES_SIZE
NUMBER_OF_TILES_WIDGHT = SCREEN_WIDTH // TILES_SIZE

ROOMS_COLOR = (230, 230, 250)
WALLS_COLOR = (150,131,236)
ROOMS_HEIGHT = [5,5,4,6,4,12,7,9]
ROOMS_WIDGHT = [17,7,4,8,6,11,9,10]
ROOMS_LOCx = [0,21,8,11,18,23,36,47]
ROOMS_LOCy = [0,0,14,11,14,13,4,1]

DOORS_LOCx = [[15,16,17],[20,21,22],[24,24,24],[35,36,37],[46,47,48],[7,8,9],[10,11,12],[17,18,19],[22,23,24]]
DOORS_LOCy = [[2,2,2],[2,2,2],[3,4,5],[7,7,7],[2,2,2],[15,15,15],[16,16,16],[15,15,15],[16,16,16]]

CORRIDORS_STARTx = [18,18,7,7,32,32,1]
CORRIDORS_STARTy = [2,2,8,8,2,2,11]

CORRIDORS_LENGTHx = [1,0,27,0,0,13,5]
CORRIDORS_LENGTHy = [0,5,0,6,5,0,0]


POTION_COLOUR=(173,255,47)      #potion vert 
MONSTER_COLOUR=(220,20,60)      #monstre rouge
WEAPON_COLOUR=(238,130,238)     #armes violet
WATER_COLOUR=(135,206,235)      #water
FOOD_COLOUR=(128,0,0)           #food
MONEY_COLOUR=(255,215,0)        #tresor jaune

MONEYy = [14,30,30,31,31]
MONEYx = [14,21,22,21,22]

POTIONy=[28,52]
POTIONx=[17,6]

WEAPONy=[12]
WEAPONx=[12]

FOODy = [10,24,39,51,15,29]
FOODx = [2,1,7,4,15,15]

WATERy = [6,26,42,50,16,26]
WATERx = [2,2,6,6,13,19]


class Game():
    def __init__(self, screen):
        self.is_running = True
        self.screen = screen
        self.piece = Piece()
        self.forbidden_cases = np.full((NUMBER_OF_TILES_HEIGHT, NUMBER_OF_TILES_WIDGHT), 0)
    
    def display_checkerboard(self):
        self.screen.fill(SCREEN_COLOR)
        k, l = int(SCREEN_HEIGHT / TILES_SIZE), int(SCREEN_WIDTH / TILES_SIZE)
        for i in range(k):
            for j in range(l):
                if (i + j) % 2 == 1:
                    rect = pygame.Rect(j * TILES_SIZE, i * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                    pygame.draw.rect(self.screen, TILES_COLOR, rect)
    
    def display_rooms(self):
        for a in range(len(ROOMS_HEIGHT)):
            for j in range(ROOMS_HEIGHT[a]):
                for i in range(ROOMS_WIDGHT[a]):
                    rect = pygame.Rect((ROOMS_LOCx[a]+ i)* TILES_SIZE, (ROOMS_LOCy[a]+ j) * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                    pygame.draw.rect(self.screen, ROOMS_COLOR, rect)
                    self.forbidden_cases[i][j] = 0
        for a in range(len(ROOMS_HEIGHT)):
            for j in range(ROOMS_HEIGHT[a]):
                rect = pygame.Rect((ROOMS_LOCx[a])*TILES_SIZE,(ROOMS_LOCy[a]+j) * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                pygame.draw.rect(self.screen, WALLS_COLOR, rect)
                rect = pygame.Rect((ROOMS_LOCx[a]+ROOMS_WIDGHT)*TILES_SIZE,(ROOMS_LOCy[a]+j) * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                pygame.draw.rect(self.screen, WALLS_COLOR, rect)
            for i in range(ROOMS_WIDGHT[a]):
                rect = pygame.Rect((ROOMS_LOCx[a]+i)*TILES_SIZE,(ROOMS_LOCy[a]) * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                pygame.draw.rect(self.screen, WALLS_COLOR, rect)
                rect = pygame.Rect((ROOMS_LOCx[a]+i)*TILES_SIZE,(ROOMS_LOCy[a]+ROOMS_HEIGHT) * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                pygame.draw.rect(self.screen, WALLS_COLOR, rect)
    
    def display_corridors(self): # vert clair
        for a in range(len(CORRIDORS_STARTx)):
            for j in range(CORRIDORS_LENGTHy[a]):
                for i in range(CORRIDORS_LENGTHx[a]):
                    rect = pygame.Rect((CORRIDORS_STARTx[a]+ i)* TILES_SIZE, (CORRIDORS_STARTy[a]+ j) * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                    pygame.draw.rect(self.screen, ROOMS_COLOR, rect)
                    self.forbidden_cases[i][j] = 0

                  

    def display(self):
        self.display_checkerboard()
        self.display_rooms()
        #self.display_corridors()
        self.piece.display(self.screen)
        self.display_object()


    def display_object(self):
            #potion vert
        for i in range (len(POTIONx)):
            x = POTIONx[i] * TILES_SIZE
            y = POTIONy[i] * TILES_SIZE
            rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
            pygame.draw.rect(self.screen,POTION_COLOUR,rect)
            self.forbidden_cases[POTIONx[i]][POTIONy[i]]= 1

            #armes violet
        for i in range (len(WEAPONx)):
            x = WEAPONx[i] * TILES_SIZE
            y = WEAPONy[i] * TILES_SIZE
            rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
            pygame.draw.rect(self.screen,WEAPON_COLOUR,rect)
            self.forbidden_cases[WEAPONx[i]][WEAPONy[i]]= 2

            #water
        for i in range (len(WATERx)):
            x = WATERx[i] * TILES_SIZE
            y = WATERy[i] * TILES_SIZE
            rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
            pygame.draw.rect(self.screen,WATER_COLOUR,rect)
            self.forbidden_cases[WATERx[i]][WATERy[i]]= 3

            #food
        for i in range (len(FOODx)):
            x = FOODx[i] * TILES_SIZE
            y = FOODy[i] * TILES_SIZE
            rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect)
            self.forbidden_cases[FOODx[i]][FOODy[i]]= 4

            #tresor jaune
        for i in range (len(MONEYx)):
            x = MONEYx[i] * TILES_SIZE
            y = MONEYy[i] * TILES_SIZE
            rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
            pygame.draw.rect(self.screen,MONEY_COLOUR,rect)
            self.forbidden_cases[MONEYx[i]][MONEYy[i]]= 5


    def update(self):
        self.piece.new_position(self.screen)


class Piece:
    def __init__(self):
        self.shape = np.array([1])
        self.position = [
            0,
            NUMBER_OF_TILES_WIDGHT // 2 - 1,
        ]  # middle pour l'instant, à modifier
        self.deplacement = 0 # pas de déplacement initial (prend des valeurs entre 0 et 4, 0 à l'arret, 1G, 2D, 3H, 4B)
        self.vie = 5 # barre de vie qui est vouée à décroitre (ou augmenter)
        self.colour = (0,0,139) # il est bleu !!!

    def display(self, screen):
        x = self.position[0] * TILES_SIZE
        y = self.position[1] * TILES_SIZE
        rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(screen,self.colour,rect)

    def new_position(self, screen):
        former_position = np.copy(self.position)
        if self.deplacement == 1: # gauche
            self.position = [former_position[0], former_position[1]-1]
            self.deplacement =0
        elif self.deplacement == 2: # droite
            self.position = [former_position[0], former_position[1]+1]
            self.deplacement =0
        elif self.deplacement == 3: # haut
            self.position = [former_position[0]-1, former_position[1]]
            self.deplacement =0
        elif self.deplacement == 4: # bas
            self.position = [former_position[0]+1, former_position[1]]
            self.deplacement =0
        

        if self.has_collided(screen) : #si il rentre dans un mur, # pour l'instant true/false mais lv up possible
            self.position = former_position
        
    def has_collided(self, screen):     #regarde contre quoi il se cogne.
        return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game(screen)
    game.piece 

    while game.is_running:
        pygame.display.set_caption("Rogue by GASCO")
        clock.tick(CLOCK_FREQUENCY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.is_running = False
            if event.type == pygame.KEYDOWN:
                # Control
                if event.key == pygame.K_LEFT:
                    game.piece.deplacement = 1
                if event.key == pygame.K_RIGHT:
                    game.piece.deplacement = 2
                if event.key == pygame.K_UP:
                    game.piece.deplacement = 3
                if event.key == pygame.K_DOWN:
                    game.piece.deplacement = 4
                
        game.update()
        game.display()
        pygame.display.update()


main()