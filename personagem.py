import pygame
from pygame.locals import *
from sys import exit
import requests

pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('audio/10-Overworld-Bgm.mp3') # Site com os sons https://downloads.khinsider.com/game-soundtracks/album/super-mario-world-original-soundtrack
#pulo_personagem = pygame.mixer.music.load('audio/pulo_yoshi.mp3')
pygame.mixer.music.play(-1)

request = requests.get('https://raw.githubusercontent.com/joseluiz123/GamePro/main/pergunta1.json')
address_data = request.json()

pergunta = address_data[f'pergunta1']
#print(f'Pergunta:' + pergunta)
game_font = pygame.font.Font(None,28)

if len(pergunta) > 20:
    pergunta = pergunta.split('*', 2)
    for x in range(2):
        print(pergunta[x])

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

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound('audio/pulo_yoshi.mp3')
        self.som_pulo.set_volume(1)
        self.sprites = []
        self.sprites.append(pygame.image.load('yoshi/sprite_0.png')) #homem_terno/homem_terno0.png
        self.sprites.append(pygame.image.load('yoshi/sprite_1.png'))
        self.sprites.append(pygame.image.load('yoshi/sprite_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7)) #(32 * 7, 32 * 7)

        self.rect = self.image.get_rect()
        self.pos_y_inicial = 368
        self.rect.topleft = 300, 368  #255 posição x e y do personagem
        self.pulo = False
        self.andar_frente = False
        self.andar_tras = False

    def andar_para_tras(self):
        self.andar_tras = True

    def andar_para_frente(self):
        self.andar_frente = True

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo == True:
            if self.rect.y <= 290:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 10
            else:
                self.rect.y = self.pos_y_inicial


        #andar para trás
        if self.andar_tras == True:
            self.rect.x -= 5
            if self.rect.x < 200:
                self.andar_tras = False
        print(self.rect.x)

        # andar para frente
        if self.andar_frente == True:
            self.rect.x += 10
            if self.rect.x > 650:
                self.andar_frente = False
        print(self.rect.x)

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

#nuvem = pygame.image.load('nuvem.png').convert()
#nuvem = pygame.transform.scale(nuvem, (700, 300))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:

                if personagem.rect.y != personagem.pos_y_inicial:
                    pass
                else:
                    personagem.pular()
            if event.key == K_a:
                personagem.andar_para_tras()
            if event.key == K_d:
                personagem.andar_para_frente()
    pygame.draw.rect(imagem_fundo, (255,245,245), (25,10,700,210))

    tela.blit(imagem_fundo, (0, 0))
 #   tela.blit(nuvem, (10, -30))

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



{
  "pergunta1": "É correto afirmar que a definição de variáveis em PHP * é feita inserindo o caractere $ no início do nome da variável",
  "resposta_correta1": "verdadeiro",
  "pergunta2": "As tuplas, embora sejam semelhantes às listas, estão limitadas a, no máximo, cinco níveis.",
  "resposta_correta2": "falso",
  "pergunta3": "Um desenvolvedor implementou um programa para exibir a média de um dado retirado de uma grande base de dados. \n Para isso, foi utilizada a linguagem Python. O trecho do código que mostra o resultado é apresentado a seguir.\n Assinale a alternativa correta acerca desse trecho de código sabendo que a média do usuário foi 75.\n print('Sua média foi {}.'.format(med)) \n (A) O programa imprime: Sua média foi 75. \n (B) O programa imprime: Sua média foi {}. \n (C) O programa imprime: Sua média foi Null. \n (D) O programa apresenta um erro na impressão porque tenta converter tipo numérico em caractere. \n (E) O programa apresenta um erro na impressão, pois não apresenta o formato do valor.",
  "resposta_correta3": "A"
}

'''
