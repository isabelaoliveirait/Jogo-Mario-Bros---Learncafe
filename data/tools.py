import os
import pygame as pg

#eventos de teclado recebendo uma lista
keybinding = {

    'action': pg.K_s,
    'jump': pg.K_SPACE,
    'left': pg.K_LEFT,
    'right': pg.K_RIGHT,
    'down' : pg.K_DOWN

}

#Classe principal que controla o jogo contendo o looping do jogo e os eventos

def_init_(self, caption):
    self.screen = pg.display.get_surface()
    self.done = False
    self.clock = pg.time.Clock()
    self.caption = caption
    self.fps = 60 #frames por segundo
    self.show_fps = False
    self.current_time = 0.0


