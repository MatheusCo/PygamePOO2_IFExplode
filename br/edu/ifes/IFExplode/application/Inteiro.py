__author__ = 'Lucas'

#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Lucas"
__date__ = "$26/09/2015 16:52:42$"

import pygame, sys, os, time

from br.edu.ifes.IFExplode.cdp.color import *
from br.edu.ifes.IFExplode.cdp.Player import *
from br.edu.ifes.IFExplode.cdp.Block import *
#from br.edu.ifes.IFExplode.cdp.Fase import *
from br.edu.ifes.IFExplode.cdp.Fase_1 import *

from pygame.locals import *


pygame.init()

# Definicoes da Janela
#window_tamanho = window_largura, window_altura = 1024, 768
window = pygame.display.set_mode(window_tamanho, pygame.RESIZABLE)
pygame.display.set_caption('IFExplode!!!')
clock = pygame.time.Clock()#funcao clock controla o tempo dentro da janela
frames_por_segundo = 60

lista_objetos_ativos = pygame.sprite.Group() #cria lista de objetos ativo
player = Player() #cria o player
player.set_image(os.path.join("Images", "PlayerV1.png"))
player.set_position(40, 40) #define uma posicao para o player

lista_objetos_ativos.add(player) #adiciona player na lista de objetos ativos

lista_Fases = [] #uma lista para as fases
lista_Fases.append(Fase_1( player )) #adiciona a fase 1 a lista e passa o objeto player naquela fase

fase_atual_numero = 0 # um numero para identificar a fase atual
fase_atual = lista_Fases[fase_atual_numero] #guarda a posicao da fase atual da lista

player.set_fase(fase_atual)


running = True # Variavel para o loop da janela principal

while running:
    for event in pygame.event.get():
        if (event.type == QUIT) or \
        (event.type == pygame.KEYDOWN and \
        (event.key == pygame.K_ESCAPE or event.key == pygame.K_q)):
            running = False

    #Funcoes de atualizacao

    player.update(fase_atual.lista_de_objetos, event)
    event = None #esvazia a variavel event
    fase_atual.update()


    #Testes de logica do jogo

    fase_atual.controla_camera()

    #Desenha e redesenha tudo

    fase_atual.draw(window)
    lista_objetos_ativos.draw(window)


    #Atrasa a Framerate

    clock.tick(frames_por_segundo)

    #Atualiza a tela

    pygame.display.update()


pygame.quit()

