import pygame
from pygame.locals import *
from sys import exit
import requests
import random

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('audio/10-overworld-bgm.mp3')  # site com os sons https://downloads.khinsider.com/game-soundtracks/album/super-mario-world-original-soundtrack
pygame.mixer.music.play(-1)

request = requests.get('https://raw.githubusercontent.com/joseluiz123/gamepro/main/pergunta1.json')
address_data = request.json()

pontos = 0
n_pergunta = 1
total_perguntas = 5

largura = 760
altura = 480

pos_resp_correta = [320]
pos_resp_correta = random.choice(pos_resp_correta)  # implementação de posição aleatória da resposta

pos_resp_errada = [25]
pos_resp_errada = random.choice(pos_resp_errada)  # implementação de posição aleatória da resposta errada

preto = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Perguntas e respostas')


class personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound('audio/pulo_yoshi.mp3')
        self.som_pulo.set_volume(1)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/sprite_0.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_1.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_2.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_2.png'))

        self.sprites.append(pygame.image.load('imagens/sprite_3.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_4.png'))
        self.sprites.append(pygame.image.load('imagens/sprite_5.png'))

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
        # personagem.coliderec

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
            #self.atual = self.atual + 0.5
            #self.atual = 3
            print('tá andando para trás')
            if self.rect.x < 10:
                self.andar_tras = False
            if self.andar_tras == True:
                self.rect.x -= 10

        # andar para frente
        if self.andar_frente == True:
            #self.atual = 0
            self.atual = self.atual + 0.5
            self.andar_frente = False
            if self.rect.x > 660:  # 595
                self.andar_frente = False
            else:
                self.rect.x += 10

        '''funcionando '''
        '''self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))
        print(self.atual)'''

        #=======================================
        #self.atual = self.atual + 0.5

        '''if self.atual >= 2: #len(self.sprites):
            self.atual = 0'''

        print(self.andar_tras)

        if self.atual > 2:# and self.andar_frente:
            self.atual = 0

        if self.andar_tras: #self.atual >= 3:
            for x in range(6):
                #self.atual = 3.5

                if self.atual > 5:
                    self.atual = 3.5 #x -= x
                else:
                    self.atual = x + 0.5  # self.atual + 0.5
                self.atual = x + 0.5
                #print(self.atual)
                self.andar_para_tras()
        print(self.atual)

        #funcionando andando para frente e para trás ele fica estático na sprite
        '''if self.atual > 2:
            self.atual = 0

        if self.andar_tras: #self.atual >= 3:
            self.atual = 3.5
            self.atual = self.atual + 0.5
            print(self.atual)
            self.andar_para_tras() '''


        '''if self.atual > 4:
            self.atual = 1'''

        #self.atual = self.atual + 0.5
        '''elif self.atual > 2:
            self.atual = 3'''



        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (10 * 7, 10 * 7))
        print(self.atual)

class resposta_correta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/resposta_correta.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (150, 35))  # (32 * 7, 32 * 7)
        self.rect = self.image.get_rect()
        self.rect.topleft = 320, 242  # x, y
        '''self.pos_resp_correta = [25, 320, 600]
        self.pos_resp_correta = random.choice(self.pos_resp_correta)
        self.rect.topleft = pos_resp_correta, 242 #300, 242'''

    def update(self):
        print('atualizou')
        self.pos_resp_correta = [25, 320]  # 250
        self.pos_resp_correta = random.choice(self.pos_resp_correta)
        print('resposta correta', self.pos_resp_correta)

        self.rect.topleft = self.pos_resp_correta, 242  # pos_resp_correta

    def esquerda(self):
        print('correta na esquerda')
        self.rect.topleft = 25, 242  # pos_resp_correta

    def meio(self):
        print('correta no meio')
        self.rect.topleft = 320, 242  # pos_resp_correta

class resposta_errada(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/resposta_correta.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (150, 35))  # (32 * 7, 32 * 7)

        self.rect = self.image.get_rect()

        '''self.pos_resp_errada = [25, 320]
        self.pos_resp_errada = random.choice(self.pos_resp_errada)'''
        self.rect.topleft = 25, 242

    def update(self):
        print('atualizou a resposta errada')
        self.pos_resp_errada = [25, 320]
        self.pos_resp_errada = random.choice(self.pos_resp_errada)
        self.rect.topleft = self.pos_resp_errada, 242
        print('resposta errada:', self.pos_resp_errada)

    def meio(self):
        print('errada no meio')
        self.rect.topleft = 320, 242  # pos_resp_correta

    def esquerda(self):
        print('errada na esquerda')
        self.rect.topleft = 25, 242


class resposta_errada2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/resposta_correta.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (150, 35))  # (32 * 7, 32 * 7)

        self.rect = self.image.get_rect()
        self.rect.topleft = 700, 242  # 25, 242

    def update(self):
        print('atualizou a resposta errada 2')


todas_as_sprites = pygame.sprite.Group()

resposta_correta = resposta_correta()
grupo_resp_correta = pygame.sprite.Group()
grupo_resp_correta.add(resposta_correta)

resposta_errada = resposta_errada()  # não existia
grupo_resp_errada = pygame.sprite.Group()  # não existia
grupo_resp_errada.add(resposta_errada)  # não existia

resposta_errada2 = resposta_errada2()
grupo_resp_errada2 = pygame.sprite.Group()
grupo_resp_errada2.add(resposta_errada2)

personagem = personagem()
todas_as_sprites.add(personagem)

pygame.draw.rect(tela, (0, 255, 0), (10, 5, 100, 20))

imagem_fundo = pygame.image.load('imagens/cidade_fundo.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

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

    if n_pergunta > total_perguntas:
        texto = f'Parabéns você fez {pontos} pontos!!!'
        # texto = f'Pergunta {n_pergunta}: {pergunta[0]}'
        texto_formatado = game_font.render(texto, True, (0, 0, 0))

        game_font = pygame.font.SysFont('arial', 25, False, False)

        texto2 = f''
        texto_formatado2 = game_font.render(texto2, True, (0, 0, 0))

        texto3 = f''
        texto_formatado3 = game_font.render(texto3, True, (0, 0, 0))


    else:
        pergunta = address_data[f'pergunta{n_pergunta}']
        resposta = address_data[f'resposta_correta1_{n_pergunta}']
        resposta_errada1 = address_data[f'resposta_errada1_{n_pergunta}']
        resposta_errada2 = address_data[f'resposta_errada2_{n_pergunta}']

        game_font = pygame.font.SysFont('arial', 25, False, False)

        pergunta = pergunta.split('*', 3)

        # print(pergunta)
        texto = f'Pergunta {n_pergunta}: {pergunta[0]}'
        texto_formatado = game_font.render(texto, True, (0, 0, 0))

        texto2 = f'{pergunta[1]}'
        texto_formatado2 = game_font.render(texto2, True, (0, 0, 0))
        # print(len(pergunta)) # exibe a quantidade da string

        texto3 = f'{pergunta[2]}'
        texto_formatado3 = game_font.render(texto3, True, (0, 0, 0))
        # print(len(pergunta)) # exibe a quantidade da string

        resposta = f'{resposta}'
        resposta_formatada = game_font.render(resposta, True, (0, 0, 0))

        resposta_errada1 = f'{resposta_errada1}'
        resp_errada1_formatada = game_font.render(resposta_errada1, True, (0, 0, 0))

        resposta_errada2 = f'{resposta_errada2}'
        resp_errada2_formatada = game_font.render(resposta_errada2, True, (0, 0, 0))

    # verifica se o personagem colidiu na resposta correta
    colisao = pygame.sprite.spritecollide(personagem, grupo_resp_correta, False)
    if colisao and n_pergunta <= total_perguntas:
        pontos += 1
        n_pergunta += 1
        print('N° Pergunta', n_pergunta)
        print(pontos)
        pos_resp_correta = [25, 320]
        pos_resp_correta = random.choice(pos_resp_correta)  # implementação de posição aleatória da resposta

        if pos_resp_correta == 25:
            pos_resp_errada = 320
            pos_resp_errada_2 = 320
            resposta_errada.meio()
            resposta_correta.esquerda()

        elif pos_resp_correta == 320:
            pos_resp_errada = 25
            pos_resp_errada_2 = 320
            resposta_errada.esquerda()
            resposta_correta.meio()

        else:
            pos_resp_errada = 25
            pos_resp_correta = 320

    #condição se o personagem colidir com a resposta errada
    colisao_errada = pygame.sprite.spritecollide(personagem, grupo_resp_errada, False)
    if colisao_errada and n_pergunta <= total_perguntas:
        n_pergunta += 1
        print('N° Pergunta', n_pergunta)
        print(pontos)
        pos_resp_correta = [25, 320]
        pos_resp_correta = random.choice(pos_resp_correta)  # implementação de posição aleatória da resposta

        if pos_resp_correta == 25:
            pos_resp_errada = 320
            pos_resp_errada_2 = 320
            resposta_errada.meio()
            resposta_correta.esquerda()

        elif pos_resp_correta == 320:
            pos_resp_errada = 25
            pos_resp_errada_2 = 320
            resposta_errada.esquerda()
            resposta_correta.meio()

        else:
            pos_resp_errada = 25
            pos_resp_correta = 320

        #resposta_correta.esquerda()

        #grupo_resp_correta.update()
        #resposta_correta.update()
        #resposta_errada.update()

    #elif personagem.colidiu == True:
        # pos_resp_correta = [25, 320]
        # pos_resp_correta = random.choice(pos_resp_correta)  # implementação de posição aleatória da resposta
    #    print('nem bateu ainda')
    tela.blit(imagem_fundo, (0, 0))

    texto_pontos = f'Pontos: {pontos}'
    texto_pontos = game_font.render(texto_pontos, True, (0, 0, 0))

    tela.blit(texto_formatado, (30, 15))  # exibe a pergunta
    tela.blit(texto_formatado2, (30, 50))  # exibe a pergunta
    tela.blit(texto_formatado3, (30, 85))  # exibe a pergunta

    # print('Reposta correta:', pos_resp_correta)
    # print('Resposta errada:', pos_resp_errada)

    '''if pos_resp_correta == 25:
        pos_resp_errada = 320
        pos_resp_errada_2 = 320

    elif pos_resp_correta == 320:
        pos_resp_errada = 25
        pos_resp_errada_2 = 320
    else:
        pos_resp_errada = 25
        pos_resp_errada_2 = 320'''

    grupo_resp_correta.draw(tela)  # exibe na tela o retângulo da resposta
    grupo_resp_errada.draw(tela)
    # grupo_resp_errada2.draw(tela)

    tela.blit(resposta_formatada, (pos_resp_correta + 15, 245))  # 50, 245 exibe a resposta
    tela.blit(resp_errada1_formatada, (pos_resp_errada + 15, 245))  # 330,245 exibe a resposta errada 1
    # tela.blit(resp_errada2_formatada, (pos_resp_errada_2, 245))  # exibe a resposta errada 2

    tela.blit(texto_pontos, (600, 150))  # exibe os pontos

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
