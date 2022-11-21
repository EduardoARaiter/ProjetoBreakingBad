
import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Breaking Bad Game")
altura = 720
largura = 720
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
back = pygame.image.load("assets/cenario.png")
heizen = pygame.image.load("assets/Hcueca.png")
hank = pygame.image.load("assets/hank.png")
comida = pygame.image.load("assets/meta.png")



def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (880,80))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("PERDEU !!!!",True,branco)
    textoDisplay2 = fonte2.render("Pressione enter!",True,branco)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    heizenX = 500
    heizenY = 400
    movimentoheizenX = 0
    larguraheizen = 110
    alturaheizen = 183
    alturahank = 110
    largurahank = 126
    posicaohankX = 400
    posicaohankY = -240
    velocidadehank = 1
    pontos = 0
    pygame.mixer.music.load("assets/music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

   

    soundGameOver = pygame.mixer.Sound("assets/gameover.mp3")
    soundGameOver.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoheizenX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoheizenX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoheizenX = 0
            
        if jogando:
            if posicaohankY > altura:
                posicaohankY = -240
                posicaohankX = random.randint(0,largura)
                #velocidadehank = velocidadehank + 1
                pontos = pontos + 1
                
            else:
                posicaohankY =posicaohankY + velocidadehank

            print(largura-larguraheizen)
            if heizenX + movimentoheizenX >0 and heizenX + movimentoheizenX< largura-larguraheizen:
                heizenX = heizenX + movimentoheizenX
            gameDisplay.fill(branco)
            gameDisplay.blit(back,(0,0))
            gameDisplay.blit(heizen, (heizenX,heizenY))
            
            gameDisplay.blit(hank, (posicaohankX,posicaohankY))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXheizen = list(range(heizenX, heizenX+larguraheizen))
            pixelsYheizen = list(range(heizenY, heizenY+alturaheizen))

            pixelXhank = list(range(posicaohankX, posicaohankX+largurahank))
            pixelYhank = list(range(posicaohankY, posicaohankY+alturahank))

            colisaoY = len(list(set(pixelYhank) & set(pixelsYheizen) ))
            if colisaoY > 10:
                colisaoX = len(list(set(pixelXhank) & set(pixelsXheizen) ))
                print(colisaoX)
                if colisaoX > 10:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(soundGameOver)


        pygameDisplay.update()
        clock.tick(60)

jogar()