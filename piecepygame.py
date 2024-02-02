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


    