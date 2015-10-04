__author__ = 'Lucas'

import pygame
from color import *

class Player (pygame.sprite.Sprite):
    # define as propriedades da imagem como cor e tamanho
    def __init__(self, color = blue, largura = 70, altura = 86):

        super( Player, self ).__init__() #pega as caracteristicas do pai e construtor
        self.image = pygame.Surface((largura, altura))
        self.image.fill(color) #preenche a imagem com uma cor

        self.set_properties()

        self.hspeed = 0
        self.vspeed = 0

        self.fase = None

    def set_properties(self):

        self.rect = self.image.get_rect() #da propriedades de um retangulo a imagem feito pelao pygame
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

        self.speed = 5


    #Define a posicao em que o objetos sera criado
    def set_position(self, x, y ):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def set_fase(self, fase):
        self.fase = fase
        self.set_position(fase.player_inicio_x, fase.player_inicio_y)

    #Carrega a imagem na sprite passando o caminho aonde esta a imagem
    def set_image(self, filename = None):
        if (filename != None):

            self.image = pygame.image.load(filename)
            self.set_properties()

    def update(self, collidable = pygame.sprite.Group() , event = None): #atualiza a imagem detectando a colisao parando o objeto

        self.aplicar_gravidade()

        self.rect.x += self.hspeed

        collision_list = pygame.sprite.spritecollide(self, collidable, False ) #lista de objetos colidiveis

        for collided_object in collision_list:
            if ( self.hspeed > 0):
                #pra la deretcha!
                self.rect.right = collided_object.rect.left
            elif (self.hspeed < 0):
                #pra la esquercha!
                self.rect.left = collided_object.rect.right

        self.rect.y += self.vspeed
        collision_list = pygame.sprite.spritecollide(self, collidable, False ) #lista de objetos colidiveis

        for collided_object in collision_list:
            if ( self.vspeed > 0):
                #pra bajo!
                self.rect.bottom = collided_object.rect.top
                self.vspeed = 0
            elif (self.vspeed < 0):
                #pra riba!
                self.rect.top = collided_object.rect.bottom
                self.vspeed = 0

        if not ( event == None ):
            if(event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    self.hspeed = -self.speed
                if (event.key == pygame.K_RIGHT):
                    self.hspeed = self.speed
                if (event.key == pygame.K_UP):
                    if(len(collision_list)>=1):
                        self.vspeed = -(self.speed)*2.0 # dobra a velocidade e pula
                '''
                if (event.key == pygame.K_DOWN):
                    #self.change_speed( 0, 5 )
                    pass
                '''

            if(event.type == pygame.KEYUP):
                if (event.key == pygame.K_LEFT):
                    if (self.hspeed < 0): self.hspeed = 0
                if (event.key == pygame.K_RIGHT):
                    if (self.hspeed > 0): self.hspeed = 0
                '''
                comentado pois temos gravidade, pode ser usado depois
                if (event.key == pygame.K_UP):
                    #if (self.vspeed != 0): self.vspeed = 0
                    pass
                if (event.key == pygame.K_DOWN):
                    #if (self.vspeed != 0): self.vspeed = 0
                    pass
                '''
    def aplicar_gravidade(self, gravidade = 0.50):
        if (self.vspeed == 0): self.vspeed = 1
        else: self.vspeed += gravidade

