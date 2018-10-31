__author__ = 'Robson_Marinho && Isabela Oliveira'

import pygame as pg
import os

#Configuracoes principais do jogo

    #CONFIGURANDO TECLADO

keybiding = {

    'action':pg.K_s,    #Tecla de ação
    'jump'  :pg.K_SPACE,  #Tecla de Pulo
    'left'  :pg.K_LEFT,   #Tecla de esquerda
    'right' :pg.K_RIGHT,  #Tecla de direita
    'down'  :pg.K_DOWN    #Tecla de abaixar
}

### CLASSE PRINCIPAL QUE CONTROLA O JOGO, CONTÉM O LOOP DO JOGO E OS EVENTOS ###

##Iniciando a classe Control com método init
class Control(object):
    def __init__(self, caption):
        self.screen = pg.display.get_surface()  #Verifica a posição da tela
        self.done = False   #Verifica se está jogando ou não
        self.Clock = pg.time.Clock()    #verifica o tempo do jogo
        self.caption = caption
        self.fdp = 60   #Controla a velocidade do jogo
        self.show_fps = False
        self.current_time = 0.0 #Tempo zerado ao (re)iniciar
        self.keys = pg.key.get_pressed()    #Verifica se tem alguma tecla pressionada
        self.state_dict = {}    #Verifica em qual estado está o jogo
        self.state_name = None  #Verifica id, acento entre outras informações
        self.state = None   #Exibe o estado jogando ou não jogando

def setup_states(self, state_dict, start_state):
    self.state_dict = state_dict    #Recebe o state_dict
    self.state_name = start_state   #Recebe o nome do estado inicial
    self.state = self.state_dict[self.state_name]

def update(self):
    self.current_time = pg.time.get_ticks()
    if self.state.quit: #se fecha a tela do jogo, se torna True
        sel.done = True
    elif self.state.done:
        self.flip_state()
    self.state.update(self.screen, self.keys, self.current_time)

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state   #Recebe o nome do estado inicial
        self.state = self.state_dict[self.state_name]

    #Função de atualização que utiliza o clock atual
    def update(self):
        self.current_time = pg.time.get_ticks() #Define os segundos da fase
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()   #Verificando o estado do menu (a troca de player 1 para player 2)
        self.state.update(self.screen, self.keys, self.current_time)

    ''' TROCA DE ESTADOS DO MENU '''
    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous

    #Função onde se apertar o 'x' para sair, o done fica True e executa a função event_loop
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:  #Verifica se alguma telca foi pressionada
                self.keys = pg.key.get_pressed()
                self.toggle_show_fps(event.key) #Tecla de verificação
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
                self.state.get_event(event)

    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps   #Não exibe o título
            if not self.show_fps:
                pg.display.set_caption(self.caption)

    def main(self):
        """Main loop for entire program"""
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            if self.show_fps:   #Se for True executa o clock e exibe os frames por segundo
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                pg.display.set_caption(with_fps)

    ## Declaração dos objetos ##
class _State(object):
    def __init__(self):
        self.start_time = 0.0   #Tempo inicial
        self.current_time = 0.0 #Tempo atual
        self.done = False   #Verifica se a tela está aberta ou o jogo está sendo executado
        self.quit = False   #Quandoe stiver TRUE é porque o jogo foi fechado
        self.next = None
        self.previous = None
        self.persist = {}   #Array ou tupla para guardar informações

    def get_event(self, event):
        pass    # o get event utilizado pra chamar um evento, n podendo ficar vazio. Por isso, insere o pass

    #fução que verifica a inicialização do jogo
    def startup(self, current_time, persistant):
        self.persist - persistant   #Persist, a variável contém os objetos
        self.start_time = current_time  #Tempo sempre começa do zero e vai para current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass

###Carregamento dos diretórios// Qual diretório usar, a cor, e o tipo de arquivo###
def load_all_gfx(directory, colorkey =(255, 0, 255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}   #Tupla para guardar as imagens
    for pic in os.listdir(directory):   #Lista o diretório
        name, ext = os.path.splitext(pic) #arquivos para serem passados dentro do diretorio: nome e extensão
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics

#Função para chamar os sons
def load_all_music(directory, accept = ('.wav', '.mp3', '.ogg', '.mdi')):
    songs = {}
    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs

def load_all_fonts(directory, accept=('.ttf')): #fonte usada apenas para carregar as pastas
    return load_all_fonts(directory, accept)

def load_all_sfx(directory, accept=('.wav', '.mpe', '.ogg', '.mdi')): #sons do jogo / carregamento
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects

def load_all


