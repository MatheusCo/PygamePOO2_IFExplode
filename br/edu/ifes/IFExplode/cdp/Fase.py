__author__ = 'Lucas'

import pygame
from color import *

window_tamanho = window_largura, window_altura = 1024, 768

class Fase(object): #utiliza o novo jeito do python de usar heranca colocando object para conseguir chamar as funcoes da classe pai

    def __init__(self, objeto_player):

        self.lista_de_objetos = pygame.sprite.Group() # grupo para os objeto das plataformas da fase
        self.objeto_player = objeto_player
        self.player_inicio = self.player_inicio_x, self.player_inicio_y = 0,0

        self.deslocamento_mundo_x = self.deslocamento_mundo_y = 0 #o quanto o mundo da fase muda

        self.visao_esquerda = window_largura/2 - window_largura/8
        self.visao_direita = window_largura/2 - window_largura/10

        self.visao_cima = window_altura/5
        self.visao_baixo = window_altura/4 - window_altura/10


    def update(self):
        self.lista_de_objetos.update() #atualiza todos os objetos do grupo de objetos

    def draw(self, window):

        window.fill(white) #desenha o fundo da janela

        self.lista_de_objetos.draw(window) #desenha os objetos da fase na janela

    def desloca_mundo(self, desloca_x, desloca_y):

        self.deslocamento_mundo_x += desloca_x
        self.deslocamento_mundo_y += desloca_y

        for cada_objeto in self.lista_de_objetos:
            cada_objeto.rect.x += desloca_x
            cada_objeto.rect.y += desloca_y

    def controla_camera(self):

        if(self.objeto_player.rect.x <= self.visao_esquerda):
            diferenca_visao = self.visao_esquerda - self.objeto_player.rect.x #diferenca do quanto podemos ir menos o quanto ja fomos para aquele lado
            self.objeto_player.rect.x = self.visao_esquerda
            self.desloca_mundo(diferenca_visao, 0)

        if(self.objeto_player.rect.x >= self.visao_direita):
            diferenca_visao = self.visao_direita - self.objeto_player.rect.x #diferenca do quanto podemos ir menos o quanto ja fomos para aquele lado
            self.objeto_player.rect.x = self.visao_direita
            self.desloca_mundo(diferenca_visao, 0)

        if(self.objeto_player.rect.y <= self.visao_cima):
            diferenca_visao = self.visao_cima - self.objeto_player.rect.y #diferenca do quanto podemos ir menos o quanto ja fomos para aquele lado
            self.objeto_player.rect.y = self.visao_cima
            self.desloca_mundo(0, diferenca_visao)

        if(self.objeto_player.rect.y >= self.visao_baixo):
            diferenca_visao = self.visao_baixo - self.objeto_player.rect.y #diferenca do quanto podemos ir menos o quanto ja fomos para aquele lado
            self.objeto_player.rect.y = self.visao_baixo
            self.desloca_mundo(0, diferenca_visao)

