import os
import pygame
import random
import turtle
import time
from pygame.locals import *
from sys import exit


pygame.init()

largura = 640
altura = 480

tamanho = (altura, largura) #tupla
gameDisplay = pygame.display.set_mode(tamanho)
fps = pygame.time.Clock()
pygame.display.set_caption("Breaking Bad Game")

branco = (255,255,255)
preto = (0,0,0)

gaming = True

background = pygame.image.load('assets/cenario.png')
heizen = pygame.image.load('assets/Hbravo.png')
heinzenCome = pygame.image.load('assets/Hcomeu.png')
policia = pygame.image.load('assets/hank.png')
comida = pygame.image.load('assets/meta.png')
telaDerrota = pygame.image.load('assets/Hperdeu.png')




def mostrarBackground(x,y):
 gameDisplay.blit(background, (x,y))



def mostrarHeizen(x,y):
 gameDisplay.blit(heizen, (x,y))


def mostrarHeizencome(x,y):
 gameDisplay.blit(heinzenCome, (x,y))


def mostrarPolicia(x,y):
    gameDisplay.blit(policia, (x,y))

def mostrarComida(x,y):
 gameDisplay.blit(comida, (x,y))

def mostrarTelaDerrota(x,y):
 gameDisplay.blit(telaDerrota, (x,y))


heizenX = (largura * 0.45)
heizenY = (altura * 0.8)











while gaming:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gaming = False
    



    gameDisplay.fill(preto)

    mostrarHeizen(heizenX,heizenY)
    
    
    
    
    
    
    
    
    
    gameDisplay.fill(preto)












    pygame.display.update()
    fps.tick(60)