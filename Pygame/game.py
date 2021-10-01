import pygame
import sys
from pygame.locals import *

pygame.init() # initialize pygame
clock = pygame.time.Clock() #inicializa o tempo no jogo
screen = pygame.display.set_mode((900,550)) #inicia a janela

programIcon = pygame.image.load(r"Images/icon.png") #carrega novo icone do programa
pygame.display.set_icon(programIcon) #seta o icone 

bg = pygame.image.load(r"Images/95.jpeg") #chama o backgroud para bg
ship = pygame.image.load(r"Images/drone.png") #carrega a imagem do drone

pygame.mouse.set_visible(0) #mouse invisivel


pygame.display.set_caption('Drone Simulator')
x=450
y=250
# fix indentation
running = True
while running:
    clock.tick(60)
    screen.blit(bg, (0,0))
    screen.blit(ship, (x-50, y-25))
    key = pygame.key.get_pressed()

    pos = pygame.mouse.get_pos()
    pointerImg = pygame.image.load(r"Images/cursor.png")
    screen.blit(pointerImg, (pos[0]-20,pos[1]-10))
    

    for event in pygame.event.get(): #procura um evento
        if event.type == pygame.QUIT: #se o evento for do tipo quit
            running = False #fecha o looping
            pygame.quit() #fecha o game
            sys.exit() #fecha o sistema
        elif event.type == MOUSEBUTTONDOWN: #se o evento for clique do mouse
            x,y = pygame.mouse.get_pos() #transforma x e y na posiçao do clique

    if key[pygame.K_LEFT]: #se clicar pra esquerda
        x+=-5 #decresce a posiçaõ no eixo horizontal para o sentido da direita
    elif key[pygame.K_RIGHT]: #se clicar para direita
        x+=5 #incrementa a posição no eixo horizontal para o sentido da esquerda
    elif key[pygame.K_UP]: #se clicar pra cima
        y+=-5 #decresce a posição no eixo vertical para cima
    elif key[pygame.K_DOWN]: #se clicar para baixo
        y+=5 #decresce a posiçaõ no eixo vertical para baixo


    pygame.display.update()

