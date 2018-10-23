"""Informacoes de caminho
Arquivo que cria a tela e os diretorios de recursos do jogo"""
_author_ = "Isabela e Robson"

import os
import pygame as pg
from . import tools
from . import constants as c

#Cria a tela e os diretorios de recursos

TITLE = c.TITLE

os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.init()

pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.TITLE)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()


#Variavel constante
FONTS = ''
#Variavel para as musicas do jogo
MUSIC = ''
#Variavel para as imagens e graficos do jogo
GFX = ''
#Variavel para os sons
SFX = ''

