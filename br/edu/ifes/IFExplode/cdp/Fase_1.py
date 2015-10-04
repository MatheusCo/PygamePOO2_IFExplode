__author__ = 'Lucas'

import pygame

from br.edu.ifes.IFExplode.cdp.Fase import *
from br.edu.ifes.IFExplode.cdp.Block import *


class Fase_1(Fase):

    def __init__(self, objeto_player):

        super (Fase_1, self).__init__(objeto_player)

        #define um lugas especifico aonde o player vai iniciar naquela fase
        self.player_inicio = self.player_inicio_x, self.player_inicio_y = 300,0

        level = [
            # [ x, y, largura, altura, color ]
            [2, 124, 365, 47, black],
            [200, 324, 280, 47, black],
            [600, 300, 200, 100, blue],
            [0, 1, 200, 1024, blue]

        ]

        for block in level:
            block = Block(block[0], block[1], block[2], block[3], block[4])
            self.lista_de_objetos.add(block)
