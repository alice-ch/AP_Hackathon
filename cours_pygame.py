class Piece:
    def __init__(self):
        self.shape = np.array(random.choice(PIECES))
        self.position = [
            0,
            NUMBER_OF_TILES_WIDGHT // 2 - 1,
        ]  # middle
        self.colour = random.choice(PIECES_COLOURS)

    def display(self, screen):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i, j] == 1:
                    x = (self.position[0] + i) * TILES_SIZE
                    y = (self.position[1] + j) * TILES_SIZE
                    rect = pygame.Rect(y, x, TILES_SIZE, TILES_SIZE)
                    pygame.draw.rect(screen, self.colour, rect)
