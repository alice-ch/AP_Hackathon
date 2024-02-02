ROOMS_HEIGHT = [5,5,4,6,4,12,7,9]
ROOMS_WEIGHT = [17,7,4,8,6,11,9,10]
ROOMS_LOCx = [0,21,8,11,18,23,36,47]
ROOMS_LOCy = [0,0,14,11,14,13,4,1]

DOORS_LOCx = [[15,16,17],
               [20,21,22],
               [24,24,24],
               [35,36,37],
               [46,47,48],
               [7,8,9],
               [10,11,12],
               [17,18,19],
               [22,23,24]]

DOORS_LOCy = [[2,2,2],
               [2,2,2],
               [3,4,5],
               [7,7,7],
               [2,2,2],
               [15,15,15],
               [16,16,16],
               [15,15,15],
               [16,16,16]]

CORRIDORS_STARTx = [18,18,7,7,32,32,1]
CORRIDORS_STARTy = [2,2,8,8,2,2,11]

CORRIDORS_LENGTHx = [1,0,27,0,0,13,5]
CORRIDORS_LENGTHy = [0,5,0,6,5,0,0]

MONEYx = [14,30,30,31,31]
MONEYy = [14,21,22,21,22]

FOODx = [10,24,39,51,15,29]
FOODy = [2,1,7,4,15,15]

WATERx = [6,26,42,50,16,26]
WATERy = [2,2,6,6,13,19]


def Object:
    def __init__(self):
        self.colors=([(173,255,47),      #potion vert 
                      (220,20,60),       # monstre rouge
                      (238,130,238),     # armes violet
                      (,,),                #water
                      (,,),                #food
                      (255,215,0)])      # tresor jaune
                                        
                                        
        self.shape = np.array([1])
        self.position = [
            0,
            NUMBER_OF_TILES_WIDGHT // 2 - 1,
        ]  # middle pour l'instant, à modifier
        self.deplacement = 0 # pas de déplacement initial (prend des valeurs entre 0 et 4, 0 à l'arret, 1G, 2D, 3H, 4B)
        self.vie = 5 # barre de vie qui est vouée à décroitre (ou augmenter)
        self.colour = (135,206,235)