import pygame
import random
import numpy as np

SCREEN_COLOR = (250, 220, 170)
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 540
CLOCK_FREQUENCY = 5

TILES_SIZE = 18
TILES_COLOR = (255, 225, 170)

NUMBER_OF_TILES_HEIGHT = SCREEN_HEIGHT // TILES_SIZE
NUMBER_OF_TILES_WIDTH = SCREEN_WIDTH // TILES_SIZE

ROOMS_COLOR = (200, 173, 127) # beige
WALLS_COLOR = (88,41,0) # marron
CORRIDORS_COLOR = (85,107,47) # vert foncé
DOORS_COLOR = (85,107,47)

ROOMS_HEIGHT = [5,5,4,7,4,12,7,9]
ROOMS_WIDTH = [17,7,4,8,6,11,9,10]
ROOMS_LOCx = [0,21,8,11,18,23,36,47]
ROOMS_LOCy = [0,0,14,11,14,13,4,1]

DOORS_LOCx = [[15,16,17],[20,21,22],[24,24,24],[35,36,37],[46,47,48],[7,8,9],[10,11,12],[17,18,19],[22,23,24]]
DOORS_LOCy = [[2,2,2],[2,2,2],[3,4,5],[8,8,8],[2,2,2],[15,15,15],[16,16,16],[15,15,15],[16,16,16]]

CORRIDORS_STARTx = [18,18,7,7,32,32,1,24]
CORRIDORS_STARTy = [2,2,8,8,2,2,11,6]

CORRIDORS_LENGTHx = [2,1,28,1,1,14,6,1]
CORRIDORS_LENGTHy = [1,6,1,7,6,1,1,2]


POTION_COLOUR = (173,255,47)      #potion vert 
MONSTER_COLOUR = (220,20,60)      #monstre rouge
WEAPON_COLOUR = (238,130,238)     #armes violet
WATER_COLOUR = (135,206,235)      #water
FOOD_COLOUR = (128,0,0)           #food
MONEY_COLOUR = (255,215,0)        #tresor jaune


class Game():
    def __init__(self, screen):
        self.is_running = True
        self.screen = screen
        self.piece = Piece()

    def display_checkerboard(self):
        self.screen.fill(SCREEN_COLOR)
        k, l = int(SCREEN_HEIGHT / TILES_SIZE), int(SCREEN_WIDTH / TILES_SIZE)
        for i in range(k):
            for j in range(l):
                if (i + j) % 2 == 1:
                    rect = pygame.Rect(j * TILES_SIZE, i * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                    pygame.draw.rect(self.screen, TILES_COLOR, rect)
        for i in range(3):
            rect = pygame.Rect(0, (i+k)* TILES_SIZE, l*TILES_SIZE, TILES_SIZE)
            pygame.draw.rect(self.screen, (255,255,255), rect)
    

    def display_rooms(self):
        for a in range(len(ROOMS_HEIGHT)):
            rect = pygame.Rect((ROOMS_LOCx[a])* TILES_SIZE, (ROOMS_LOCy[a]) * TILES_SIZE, TILES_SIZE*ROOMS_WIDTH[a], TILES_SIZE*ROOMS_HEIGHT[a])
            pygame.draw.rect(self.screen, ROOMS_COLOR, rect)
        # affichage des fonds de salles
        for a in range(len(ROOMS_HEIGHT)):
            rect = pygame.Rect((ROOMS_LOCx[a])*TILES_SIZE,(ROOMS_LOCy[a]) * TILES_SIZE, TILES_SIZE, TILES_SIZE*(ROOMS_HEIGHT[a]-1))
            pygame.draw.rect(self.screen, WALLS_COLOR, rect)
            rect = pygame.Rect((ROOMS_LOCx[a])*TILES_SIZE,(ROOMS_LOCy[a]) * TILES_SIZE, TILES_SIZE*(ROOMS_WIDTH[a]-1), TILES_SIZE)
            pygame.draw.rect(self.screen, WALLS_COLOR, rect)
            rect = pygame.Rect((ROOMS_LOCx[a]+ROOMS_WIDTH[a]-1)*TILES_SIZE,(ROOMS_LOCy[a]) * TILES_SIZE, TILES_SIZE, TILES_SIZE*(ROOMS_HEIGHT[a]))
            pygame.draw.rect(self.screen, WALLS_COLOR, rect)       
            rect = pygame.Rect((ROOMS_LOCx[a])*TILES_SIZE,(ROOMS_LOCy[a]+ROOMS_HEIGHT[a]-1) * TILES_SIZE, TILES_SIZE*(ROOMS_WIDTH[a]-1), TILES_SIZE)
            pygame.draw.rect(self.screen, WALLS_COLOR, rect)
        # affichage des murs
    
    def display_corridors(self):
        for a in range(len(CORRIDORS_STARTx)):
            for i in range(CORRIDORS_LENGTHx[a]):
                for j in range(CORRIDORS_LENGTHy[a]):
                    rect = pygame.Rect((CORRIDORS_STARTx[a]+ i)* TILES_SIZE, (CORRIDORS_STARTy[a]+ j) * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                    pygame.draw.rect(self.screen, CORRIDORS_COLOR, rect)
                    self.piece.forbidden_cases[CORRIDORS_STARTx[a]+i,CORRIDORS_STARTy[a]+j] = 0
    
    def display_doors(self):
        for a in range(len(DOORS_LOCx)):
            for i in range(3) :
                rect = pygame.Rect(DOORS_LOCx[a][i]* TILES_SIZE, DOORS_LOCy[a][i] * TILES_SIZE, TILES_SIZE, TILES_SIZE)
                pygame.draw.rect(self.screen, DOORS_COLOR, rect)
                self.piece.forbidden_cases[DOORS_LOCx[a][i],DOORS_LOCy[a][i]] = 0


    def display(self):
        self.display_checkerboard()
        self.display_rooms()
        self.display_corridors()
        self.display_doors()
        self.display_object()
        self.display_life()
        self.display_eau()
        self.display_food()
        self.display_money()
        self.display_xp()
        self.piece.display(self.screen)
    
    def display_object(self):
            #potion vert
        for i in range (len(self.piece.POTION)):
            a,b=self.piece.POTION[i]
            x = a * TILES_SIZE
            y = b * TILES_SIZE
            rect01 = pygame.Rect(x + 2, y + 6, 10, 10)
            rect02 = pygame.Rect(x + 4, y + 1, 5, 8)
            rect1 = pygame.Rect(x + 3, y + 7, 8, 8)
            rect2 = pygame.Rect(x + 5, y + 2, 3, 6)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect01)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect02)
            pygame.draw.rect(self.screen,POTION_COLOUR,rect1)
            pygame.draw.rect(self.screen,POTION_COLOUR,rect2)
            self.piece.forbidden_cases[a][b]= 1

            #armes violet
        for i in range (len(self.piece.WEAPON)):
            a,b=self.piece.WEAPON[i]
            x = a * TILES_SIZE
            y = b * TILES_SIZE
            rect01 = pygame.Rect(x + 7, y + 1, 4, 16)
            rect02 = pygame.Rect(x + 4, y + 11, 10, 4)
            rect1 = pygame.Rect(x + 8, y + 2, 2, 14)
            rect2 = pygame.Rect(x + 5, y + 12, 8, 2)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect01)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect02)
            pygame.draw.rect(self.screen,WEAPON_COLOUR,rect1)
            pygame.draw.rect(self.screen,WEAPON_COLOUR,rect2)
            self.piece.forbidden_cases[a][b]= 2

            #water
        for i in range (len(self.piece.WATER)):
            a,b=self.piece.WATER[i]
            x = a * TILES_SIZE
            y = b * TILES_SIZE
            rect1 = pygame.Rect(x + 9,y + 4, 7, 7)
            rect2 = pygame.Rect(x + 7, y + 7, 5, 5)
            rect3 = pygame.Rect(x + 10, y + 5, 2, 2)
            rect01 = pygame.Rect(x + 4, y + 9, 8, 8)
            rect02 = pygame.Rect(x + 7, y + 7, 6, 6)
            rect03 = pygame.Rect(x + 9, y + 8, 3, 3)
            pygame.draw.rect(self.screen,(0, 0, 139),rect01)
            pygame.draw.rect(self.screen,(0, 0, 139),rect02)
            pygame.draw.rect(self.screen,(0, 0, 139),rect03)
            pygame.draw.rect(self.screen,WATER_COLOUR,rect1)
            pygame.draw.rect(self.screen,WATER_COLOUR,rect2)
            pygame.draw.rect(self.screen,WATER_COLOUR,rect3)
            self.piece.forbidden_cases[a][b]= 3

            #food
        for i in range (len(self.piece.FOOD)):
            a,b=self.piece.FOOD[i]
            x = a * TILES_SIZE
            y = b * TILES_SIZE
            rect1 = pygame.Rect(x + 2, y + 8, 8, 8)
            rect2 = pygame.Rect(x + 9, y + 6, 5, 2)
            rect3 = pygame.Rect(x + 10, y + 4, 2, 3)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect1)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect2)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect3)
            self.piece.forbidden_cases[a][b]= 4

            #tresor jaune
        for i in range (len(self.piece.MONEY)):
            a,b=self.piece.MONEY[i]
            x = a * TILES_SIZE
            y = b * TILES_SIZE
            rect1 = pygame.Rect(x + 4, y + 9, 6, 4)
            rect2 = pygame.Rect(x + 9, y + 4, 6, 4)
            rect3 = pygame.Rect(x + 14, y + 9, 6, 4)
            rect01 = pygame.Rect(x + 3, y + 8, 8, 6)
            rect02 = pygame.Rect(x + 8, y + 3, 8, 6)
            rect03 = pygame.Rect(x + 13, y + 8, 8, 6)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect01)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect02)
            pygame.draw.rect(self.screen,FOOD_COLOUR,rect03)
            pygame.draw.rect(self.screen,MONEY_COLOUR,rect1)
            pygame.draw.rect(self.screen,MONEY_COLOUR,rect2)
            pygame.draw.rect(self.screen,MONEY_COLOUR,rect3)
            self.piece.forbidden_cases[a][b]= 5

    def display_life(self):
        rect = pygame.Rect(SCREEN_WIDTH-10*TILES_SIZE, SCREEN_HEIGHT+TILES_SIZE, self.piece.vie *TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(self.screen,(255,0,0),rect)
    
    def display_eau(self):
        rect = pygame.Rect(SCREEN_WIDTH-40*TILES_SIZE, SCREEN_HEIGHT+TILES_SIZE, self.piece.eau *TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(self.screen,WATER_COLOUR,rect)

    def display_money(self):
        rect = pygame.Rect(SCREEN_WIDTH-50*TILES_SIZE, SCREEN_HEIGHT+TILES_SIZE, self.piece.money *TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(self.screen,MONEY_COLOUR,rect)

    def display_food(self):
        rect = pygame.Rect(SCREEN_WIDTH-30*TILES_SIZE, SCREEN_HEIGHT+TILES_SIZE, self.piece.faim *TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(self.screen,FOOD_COLOUR,rect)
    
    def display_xp(self):
        rect = pygame.Rect(SCREEN_WIDTH-20*TILES_SIZE, SCREEN_HEIGHT+TILES_SIZE, self.piece.xp *TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(self.screen,POTION_COLOUR,rect)


    def update(self):
        self.piece.new_position(self.screen)


class Piece:
    def __init__(self):
        self.shape = np.array([1])
        self.position = [
            2,
            NUMBER_OF_TILES_WIDTH // 2 - 6,
        ]  # middle pour l'instant, à modifier
        self.deplacement = 0 # pas de déplacement initial (prend des valeurs entre 0 et 4, 0 à l'arret, 1G, 2D, 3H, 4B)
        self.vie = 5 # barre de vie qui est vouée à décroitre (ou augmenter)
        self.xp = 5
        self.money = 2
        self.faim=2
        self.eau=2
        self.colour = (255,255,0) # il est bleu !!!
        self.MONEY=[(14,14),(30,21),(30,22),(31,21),(31,22)]
        self.POTION=[(28,17),(52,6)]
        self.WEAPON=[(12,12)]
        self.FOOD=[(10,2),(24,1),(39,5),(51,5),(29,15)]
        self.WATER=[(6,2),(26,2),(42,6),(50,6),(16,13),(26,19)]
        self.forbidden_cases = np.full((NUMBER_OF_TILES_WIDTH, NUMBER_OF_TILES_HEIGHT), -1)
        for a in range(len(ROOMS_HEIGHT)):
            for i in range(1,ROOMS_WIDTH[a]-1):
                for j in range(1, ROOMS_HEIGHT[a]-1):
                    self.forbidden_cases[i+ROOMS_LOCx[a],j+ROOMS_LOCy[a]] = 0

    def display(self, screen):
        x = self.position[0] * TILES_SIZE
        y = self.position[1] * TILES_SIZE
        rect1 = pygame.Rect(y, x, TILES_SIZE,TILES_SIZE)
        rect2 = pygame.Rect(y+4, x+4,3,3)
        rect3 = pygame.Rect(y+11, x+4,3,3)
        rect4= pygame.Rect(y+4, x+11,10,3)
        pygame.draw.rect(screen,self.colour,rect1)
        pygame.draw.rect(screen,(0,0,139),rect2)
        pygame.draw.rect(screen,(0,0,139),rect3)
        pygame.draw.rect(screen,(0,0,139),rect4)

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
        


        x = self.position[0] # on est en nb de cases et pas en pixels
        y = self.position[1]
        if self.forbidden_cases[y][x]== -1 : # c'est un mur
            self.position = former_position
        elif self.forbidden_cases[y][x]== 0 :
            self.faim -= 0.01
            self.eau -= 0.01

        elif self.forbidden_cases[y,x]== 1 : # c'est une potion
            self.vie+=1
            i = 0
            while i < len(self.POTION):
                a,b = self.POTION[i]
                if (a,b) == (y,x) :
                    del self.POTION[i]
                i += 1
            self.forbidden_cases[y,x]=0

        elif self.forbidden_cases[y,x]== 2 : # c'est une arme
            self.vie += 1            
            i = 0
            while i < len(self.WEAPON):
                a,b = self.WEAPON[i]
                if a==x & b==y :
                    del self.WEAPON[i]
                i += 1
            self.forbidden_cases[y,x]=0 

        elif self.forbidden_cases[y,x]== 3 : # c'est de l'eau
            self.eau+=1
            i = 0
            while i < len(self.WATER):
                a,b = self.WATER[i]
                if (a,b) == (y,x) :
                    del self.WATER[i]
                    
                i += 1
            self.forbidden_cases[y,x]=0

        elif self.forbidden_cases[y,x]== 4 : # c'est à manger
            self.faim += 1
            self.forbidden_cases[y,x]=0
            i = 0
            while i < len(self.FOOD):
                a,b = self.FOOD[i]
                if (a,b)==(y,x):
                    del self.FOOD[i]
                    print(1)
                i += 1
            self.forbidden_cases[y,x]=0

        elif self.forbidden_cases[y,x]== 5 : # c'est un trésor
            self.money += 1
            self.forbidden_cases[y,x]=0
            i = 0
            while i < len(self.MONEY):
                a,b = self.MONEY[i]
                if (a,b) == (y,x) :
                    del self.MONEY[i]
                i += 1
            self.forbidden_cases[y,x]=0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT+3*TILES_SIZE))
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