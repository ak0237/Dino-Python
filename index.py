import pygame
from pygame.locals import *
from sys import exit
from random import randrange
import os

diretorio_pricipal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_pricipal, 'imagens')
diretorio_audio = os.path.join(diretorio_pricipal, 'audio')

pygame.init()

LARGURA = 640
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Jooj Dino')

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha()




class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dino = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dino.append(img)

        self.index_lista = 0
        self.image = self.imagens_dino[self.index_lista] 
        self.rect = self.image.get_rect()
        self.rect.center = (100,ALTURA - 90)

    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0

        self.index_lista += 0.25
        self.image = self.imagens_dino[int(self.index_lista)]

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = sprite_sheet.subsurface((7*32, 0), (32,32))
            self.image = pygame.transform.scale(self.image, (32*2, 32*3))
            self.rect = self.image.get_rect()
            self.rect.y = randrange(50, 200, 50) ## numero de 50 a 200 de 50 à 50 
            self.rect.x = LARGURA - randrange(30,300,90)
    ## Faz a nuvem andar
    def update(self):
        if self.rect.x < -20:
            self.rect.x = LARGURA 
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= 10

todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)


for i in range(7):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)


relogio = pygame.time.Clock()
while True:
    tela.fill(BRANCO)
    relogio.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()