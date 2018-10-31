__author__ = 'Robson_Marinho && Isabela Oliveira'


### CRIA TELA / CORES / TAMANHO / POSIÇÃO / VELOCIDADE ###

SCREEN_HEIGHT = 768  #Altura da tela
SCREEN_WIDTH = 1024   #largura da tela

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT) #Variável de tamanho e largura

TITLE = "Super Mário Bros"  #Títtulo da página

    #### CORES RGB ###

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
GREEN = ( 0, 255, 0)
FOREST_GREEN = (31, 162, 35)
BLUE = (0, 0, 255)
SKY_BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
NEAR__BLACK = (19, 15, 48)
COMBLUE = (233, 232, 255)
GOLD = (255, 215, 0)

BGCOLOR = WHITE #Variável de background


SIZE_MULTIPLAYER = 2.5  #Tamanho do multiplayer
BRICK_SIZE_MULTIPLAYER = 2.69
BACKGROUND_MULTIPLAYER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

## MARIO FORÇAS ##

WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01  #define a gravidade
JUMP_GRAVITY = .31
JUMP-VEL = -10  #Velocidade do pulo
FAST_JUMP_VEL = -12.5   #velocidade do pulo na corrida
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800 #Máximo de velocidade
MAX_WALK_SPEED = 6

### MARIO ESTADOS ###

STAND = 'standing'  #De pé
WALK = 'walk'   #andando
JUMP = 'jump'   #pulando
FALL = 'fall'
SMALL_TO_BIG = 'small to big'           #De pequeno para grande
BIG_TO_FIRE = 'big to fire'             #De grande para fogo
BIG_TO_SMALL = 'big to small'           #De grande para pequeno
FLAGPOLE = 'flag pole'                  #bandeira
WALKING_TO_CASTLE = 'walking to castle' #Andando ao castelo
END_OF_LEVEL_FALL = 'end of level fall' #Final do level