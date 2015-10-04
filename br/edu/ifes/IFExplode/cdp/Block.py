__author__ = 'Lucas'

import pygame
from color import *

class Block( pygame.sprite.Sprite): # Usa a classe sprite do java

    def __init__(self, x, y,  largura, altura, color = blue):

        super( Block, self ).__init__() #pega as caracteristicas do pai e construtor
        self.image = pygame.Surface((largura, altura))
        self.image.fill(color) #preenche a imagem com uma cor

        self.rect = self.image.get_rect() #da propriedades de um retangulo a imagem feito pelao pygame

        #self.origin_x = self.rect.centerx
        #self.origin_y = self.rect.centery

        self.rect.x = x #- self.origin_x
        self.rect.y = y #- self.origin_y
