import pygame
import random
import numpy as np

SCREEN_COLOR = (50, 50, 50)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
CLOCK_FREQUENCY = 5

TILES_SIZE = 22
TILES_COLOR = (15, 15, 15)

NUMBER_OF_TILES_HEIGHT = SCREEN_HEIGHT // TILES_SIZE
NUMBER_OF_TILES_WIDGHT = SCREEN_WIDTH // TILES_SIZE

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
                    rect = pygame.Rect(
                        j * TILES_SIZE, i * TILES_SIZE, TILES_SIZE, TILES_SIZE
                    )
                    pygame.draw.rect(self.screen, TILES_COLOR, rect)
    
    def display(self):
        self.display_checkerboard()
        self.piece.display(self.screen)


class Piece:
    def __init__(self):
        self.shape = np.array([1])
        self.position = [
            0,
            NUMBER_OF_TILES_WIDGHT // 2 - 1,
        ]  # middle pour l'instant, à modifier
        self.colour = (135,206,235) # il est bleu !!!

    def display(self, screen):
        x = self.position[0] * TILES_SIZE
        y = self.position[1] * TILES_SIZE
        rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
        pygame.draw.rect(screen,self.colour,rect)

    def new_position(self, screen):
        former_position = np.copy(self.position)

        if.... gauche:
            self.shape = [former_position[0] -1 ,former_position[1]  ]
        elif.... droite:
            self.shape = [former_position[0] + 1 ,former_position[1] ]
        elif.... haut:
            self.shape = [former_position[0] ,former_position[1] +1]
        elif.... droit :
            self.shape = [former_position[0] ,former_position[1] -1 ]


        if self.has_collided(screen) : #si il rentre dans un mur, # pour l'instant true/false mais lv up possible
            self.shape = former_position
        
    def has_collided(self, screen):
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
                    game.piece.horizontal_direction += -1
                if event.key == pygame.K_RIGHT:
                    game.piece.horizontal_direction += 1
                if event.key == pygame.K_DOWN:
                    game.piece.vertical_direction += -1
                if event.key == pygame.K_UP:
                    game.piece.vertical_direction += 1

        game.display()
        pygame.display.update()


main()