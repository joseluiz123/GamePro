import pygame
from pygame.locals import *
from sys import exit
import requests

pygame.init()

request = requests.get('https://raw.githubusercontent.com/joseluiz123/GamePro/main/pergunta1.json')
address_data = request.json()

pergunta = address_data[f'pergunta1']
#print(f'Pergunta:' + pergunta)
game_font = pygame.font.Font(None,28)

if len(pergunta) > 20:
    pergunta = pergunta.split('*', 2)
    for x in range(2):
        print(pergunta[x])

#print(pergunta.split(' ', 10))


#texto = game_font.render('red',True,'Black')
#texto_rect = texto.get_rect(center = (25,10))
texto = f'Pergunta 1: {pergunta[0]}'
texto_formatado = game_font.render(texto, True, (0, 0, 0))

texto2 = f'{pergunta[1]}'
texto_formatado2 = game_font.render(texto2, True, (0, 0, 0))
#print(len(pergunta)) # exibe a quantidade da string

largura = 760
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

#container = pygame.display.set_mode(720, 200)

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('yoshi/sprite_0.png')) #homem_terno/homem_terno0.png
        self.sprites.append(pygame.image.load('yoshi/sprite_1.png'))
        self.sprites.append(pygame.image.load('yoshi/sprite_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7)) #(32 * 7, 32 * 7)

        self.rect = self.image.get_rect()
        self.rect.topleft = 300, 380 #255

    def update(self):
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))

todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

pygame.draw.rect(tela, (0,255,0), (10, 5, 100, 20))

imagem_fundo = pygame.image.load('cidade_fundo.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(imagem_fundo, (255,245,245), (25,10,700,210))

    tela.blit(imagem_fundo, (0, 0))

    tela.blit(texto_formatado, (30,15)) #exibe a pergunta
    tela.blit(texto_formatado2, (30,50)) #exibe a pergunta

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()



''' FUNCIONANDO
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 760
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')


class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('homem_terno/homem_terno0.png'))
        self.sprites.append(pygame.image.load('homem_terno/homem_terno1.png'))
        self.sprites.append(pygame.image.load('homem_terno/homem_terno2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32 * 7, 32 * 7))

        self.rect = self.image.get_rect()
        self.rect.topleft = 300, 255

    def update(self):
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32 * 7, 32 * 7))


todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

imagem_fundo = pygame.image.load('cidade_fundo.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(imagem_fundo, (0, 0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()


'''
