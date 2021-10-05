import pygame
from pygame.locals import *
from sys import exit
import requests

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load(
    'audio/10-overworld-bgm.mp3')  # site com os sons https://downloads.khinsider.com/game-soundtracks/album/super-mario-world-original-soundtrack
pygame.mixer.music.play(-1)

request = requests.get('https://raw.githubusercontent.com/joseluiz123/gamepro/main/pergunta1.json')
address_data = request.json()

n_pergunta = 1
pontos = 0

pergunta = address_data[f'pergunta{n_pergunta}']
resposta = address_data[f'resposta_correta1_{n_pergunta}']
resposta_errada1 = address_data[f'resposta_errada1_{n_pergunta}']
resposta_errada2 = address_data[f'resposta_errada2_{n_pergunta}']

game_font = pygame.font.SysFont('arial', 25, False, False)

pergunta = pergunta.split('*', 2)
for x in range(2):
    print(pergunta[x])

print(pergunta)
texto = f'Pergunta {n_pergunta}: {pergunta[0]}'
texto_formatado = game_font.render(texto, True, (0, 0, 0))

texto2 = f'{pergunta[1]}'
texto_formatado2 = game_font.render(texto2, True, (0, 0, 0))
# print(len(pergunta)) # exibe a quantidade da string

resposta = f'{resposta}'
resposta_formatada = game_font.render(resposta, True, (0, 0, 0))

resposta_errada1 = f'{resposta_errada1}'
resp_errada1_formatada = game_font.render(resposta_errada1, True, (0, 0, 0))

resposta_errada2 = f'{resposta_errada2}'
resp_errada2_formatada = game_font.render(resposta_errada2, True, (0, 0, 0))

largura = 760
altura = 480

preto = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('sprites')


class personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound('audio/pulo_yoshi.mp3')
        self.som_pulo.set_volume(1)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/sprite_0.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_1.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_2.png'))
        ''' self.sprites.append(pygame.image.load('imagens/sprite_3.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_4.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_5.png'))'''
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))  # (32 * 7, 32 * 7)

        self.rect = self.image.get_rect()
        self.pos_y_inicial = 368
        self.rect.topleft = 320, 368  # 320, 368 posição x e y do personagem
        self.pulo = False
        self.andar_frente = False
        self.andar_tras = False
        self.colidiu = False

    def andar_para_tras(self):
        self.andar_tras = True

    def andar_para_frente(self):
        self.andar_frente = True

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def colidiu(self):
        self.colidiu = True
        #personagem.coliderec

    def update(self):
        # personagem.rect.x = 320
        if self.pulo == True:
            if self.rect.y <= 290:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 10
            else:
                self.rect.y = self.pos_y_inicial

        # andar para trás
        if self.andar_tras == True:
            if self.rect.x < 10:
                self.andar_tras = False
            if self.andar_tras == True:
                self.rect.x -= 10

        # andar para frente
        if self.andar_frente == True:
            self.andar_frente = False
            if self.rect.x > 595:
                self.andar_frente = False
            else:
                self.rect.x += 10

        '''if pygame.sprite.groupcollide(todas_as_sprites, grupo_resp_correta):
            print('colidiu')'''
        '''  #teste alterar sprite
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            #if self.andar_frente == True:
            self.atual = 0
        if self.andar_frente == True:
            self.atual = 4
        print(self.andar_frente)
        print(self.atual)

        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))'''
        #print(len(self.sprites))
        #print(self.atual)


        ### tentativa de alterar a sprite qudno estiver andando para trás ###
        '''if self.andar_tras == True:
            self.atual = 3
        if self.andar_frente == True:
            self.atual = 1
        else:
            self.atual = self.atual + 0.5'''
        #####

        ''' isso aqui funciona, mas o personagem não altera a sprite qnd vai para trás
        self.atual = self.atual + 0.5

        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        #print(self.atual)
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))'''

        '''# altera a sprite para movimentando para trás
        if self.andar_tras == True:
            self.atual = self.atual + 0.5
            if self.atual > 2:
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            print(self.atual)

            self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))

        #altera a sprite para movimentando para frente  ==revisar==
        else: # self.andar_frente == True
            self.atual = self.atual + 0.5
            print(self.atual)
            if self.atual <= 10:
                self.atual = 3
            self.image = self.sprites[int(self.atual)]

            self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))'''

        '''funcionando '''
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))

class resposta_correta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/resposta_correta.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (150, 35))  # (32 * 7, 32 * 7)
        self.rect = self.image.get_rect()
        self.rect.topleft = 300, 242 #300, 265

    def update(self):
        print('atualizou')


class resposta_errada(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/resposta_correta.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (150, 35))  # (32 * 7, 32 * 7)

        self.rect = self.image.get_rect()
        self.rect.topleft = 25, 242 #300, 265

    def update(self):
        print('atualizou a resposta errada')

todas_as_sprites = pygame.sprite.Group()

resposta_correta = resposta_correta()
grupo_resp_correta = pygame.sprite.Group()
grupo_resp_correta.add(resposta_correta)

resposta_errada = resposta_errada() #não existia
grupo_resp_errada = pygame.sprite.Group() #não existia
grupo_resp_errada.add(resposta_errada) #não existia

personagem = personagem()
todas_as_sprites.add(personagem)

pygame.draw.rect(tela, (0, 255, 0), (10, 5, 100, 20))

imagem_fundo = pygame.image.load('imagens/cidade_fundo.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

# nuvem = pygame.image.load('nuvem.png').convert()
# nuvem = pygame.transform.scale(nuvem, (700, 300))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(preto)

    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[K_a] or keys[K_LEFT]:
        personagem.andar_para_tras()
    else:
        personagem.andar_tras = False

    if keys[K_d] or keys[K_RIGHT]:
        personagem.andar_para_frente()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                if personagem.rect.y != personagem.pos_y_inicial:
                    pass
                else:
                    personagem.pular()

    pygame.draw.rect(imagem_fundo, (255, 245, 245), (25, 10, 700, 210))

    #verifica se o personagem colidiu na resposta
    colisao = pygame.sprite.spritecollide(personagem, grupo_resp_correta, False)
    if colisao:
        grupo_resp_correta.update()  # não existia
        pontos += 1
        n_pergunta += 1
        pass
        print('N° Pergunta', n_pergunta)
        print(pontos)

    tela.blit(imagem_fundo, (0, 0))
    # tela.blit(nuvem, (10, -30))

    texto_pontos = f'Pontos: {pontos}'
    texto_pontos = game_font.render(texto_pontos, True, (0, 0, 0))

    grupo_resp_correta.draw(tela) #exibe na tela o retângulo da resposta
    grupo_resp_errada.draw(tela)

    tela.blit(texto_formatado, (30, 15))  # exibe a pergunta
    tela.blit(texto_formatado2, (30, 50))  # exibe a pergunta
    tela.blit(resposta_formatada, (320, 245))  # exibe a resposta
    tela.blit(resp_errada1_formatada, (80, 245))  # exibe a resposta errada 1
    tela.blit(resp_errada2_formatada, (600, 260))  # exibe a resposta errada 2

    tela.blit(texto_pontos, (600, 150))  # exibe os pontos

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
