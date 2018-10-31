__author__ = 'Robson_Marinho && Isabela Oliveira'


from .. import setup, tools
from .. import constants as c
from .. import game_sound
from ..components import info

class LoadScreen(tools.State): #classe recebendo o estado de carregamento através do parametro State
    def __init__(self):
        tools._State.__init__(self)


    def startup(self, current_time, persist): #persist carregamento de objetos, pois é uma tupla ou array
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()


        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)


    def set_next_state(self):
        """Sets the next State"""
        return c.LEVEL1

    def set_overhead_info_state(self): #executa a variavel de carregamento de tela
        """Sets the state to send to the overhead info object"""
        return c.LOAD_SCREEN

    def update(self, surface, keys, current_time):
        """Updates the loading screen"""
        if (current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info) #mensagens e informacoes que seram utilizadas no carregamento da tela inicial
            self.overhead_info.draw(surface) 

        elif(current_time - self.start_time) < 2600:
            surface.fill(c.BLACK)

        elif(current_time - self.start_time) < 2635:
            surface.fill((106, 150, 252))
            
        else:
            self.done = True
            

class GameOver(LoadScreen):
    """Carregamento da tela de Game Over"""
    def __init__(self):
        super(GameOver, self).__init__()

    def set_next_state(self):
        """configurando proximo estado"""
        return c.MAIN_MENU  #retorna o menu do jogo no arquivo de constate

    def set_overhead_info_state(self):
        """Atualizando para fim do jogo"""
        return c.GAME_OVER #nas informacoes mostrando quais informacoes terá nele

    def update(self, surface, keys, current_time): #funcao pra atualizacao que vai verificar tempo e outros parametros
        self.current_time = current_time
        self.sound_manager.update(self.persist, None)

        if (self.current_time - self.start_time) < 7000: #podendo ser realizado mudanças e incrementos
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        elif (self.current_time - self.start_time) < 7200:
            surface.fill(c.BLACK)
        elif (self.current_time - self.start_time) < 7235:
            surface.fill((106, 150, 252))
        else:
            self.done = True

class TimeOut(LoadScreen):
    """carregamento tela com fim do tempo"""
    def __init__(self):
        super(TimeOut, self).__init__()

    def set_next_state(self):
        """passando para o proximo estagio"""
        if self.persist[c.LIVES] == 0:
            return c.GAME_OVER
        else:
            return c.LOAD_SCREEN

    def set_overhead_info_state(self):
        """definindo o estagio com o fim do tempo"""
        return c.TIME_OUT

    def update(self, surface, keys, current_time):
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface) #desenha na tela um objeto que ja foi instanciado
        else:
            self.done = True

















