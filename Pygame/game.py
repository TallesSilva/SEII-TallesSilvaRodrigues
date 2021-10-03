import pygame
import sys
from pygame.locals import *
import numpy as np

class Drone:

    def __init__(self):
        self.m = 0.3 #kg
        self.g = 9.8 #gravidade
        self.F_max = 5
        self.F_min = 0

    def gravity(self): #gravidade é massa * aceleração * F_angular 0
        v=self.m*self.g*np.sin(np.pi/2)
        return v

    def F_motor1(self, accelerate, fi): #força vertical
        #-----cálculo da força vertical do motor 2
        v=self.m*accelerate*np.sin(fi)
        #-----condiçaõ max de força do motor
        if v>=self.F_max:v=self.F_max
        elif v<=self.F_min:v=self.F_min
        return -v

    def F_angular(self, accelerate, fi): #força horizontal dos motores
        #-----Calculo da Força horizontal
        f_motor=drone.F_motor1(accelerate, pi/2)*2
        v=np.cos(fi)*f_motor
        return v


if __name__ == "__main__":
    pygame.init() # initialize pygame
    clock = pygame.time.Clock() #inicializa o tempo no jogo
    screen = pygame.display.set_mode((900,550)) #inicia a janela

    programIcon = pygame.image.load(r"Images/icon.png") #carrega novo icone do programa
    pygame.display.set_icon(programIcon) #seta o icone 
    pointerImg = pygame.image.load(r"Images/cursor.png")
    bg = pygame.image.load(r"Images/95.jpeg") #chama o backgroud para bg
    ship = pygame.image.load(r"Images/drone.png") #carrega a imagem do drone
    pygame.mouse.set_visible(0) #mouse invisivel
    running = True
    pygame.display.set_caption('Drone Simulator')
    pygame.display.flip()
    pi = np.pi
    x_limit= 50, 450
    y_limit= 435, -890 
    y_force = 0
    fi = pi/2
    aceleracao = 0
    x = 500
    y = 435
    drone = Drone()

    while running:
        clock.tick(60)
        screen.blit(bg, (0,0))
        screen.blit(pygame.transform.rotate(ship, -np.degrees(fi)), (x, y))
       
        key = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        screen.blit(pointerImg, (pos[0],pos[1]))
        

        for event in pygame.event.get(): #procura um evento
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]: #se o evento for do tipo quit
                running = False #fecha o looping
                pygame.display.quit() #fecha o game
                sys.exit() #fecha o sistema


        #------------Comando Horizontal------------------#
        if key[pygame.K_LEFT]: #se clicar pra esquerda
            fi -= pi/180  #decresce a posiçaõ no eixo horizontal para o sentido da direita
            if fi<=pi/4: fi=pi/4
        elif key[pygame.K_RIGHT]: #se clicar para direita
            fi += pi/180 #incrementa a posição no eixo horizontal para o sentido da esquerda
            if fi>=3*pi/4: fi=3*pi/4
            
        pygame.display.flip()
        #------------Comando Vertical---------------#
        if key[pygame.K_UP]: #se clicar pra cima
            aceleracao += 0.5#decresce a posição no eixo vertical para cima
        elif key[pygame.K_DOWN]: #se clicar para baixo
            aceleracao -= 0.5 #decresce a posiçaõ no eixo vertical para baixo
        if aceleracao>=10: aceleracao=10
        elif aceleracao<=-10: aceleracao=-10

        y_force = drone.F_motor1(aceleracao,fi)*2

        #------------Comando Waypoint-----------------#
        if event.type == MOUSEBUTTONDOWN: #se o evento for clique do mouse
            x,y = pygame.mouse.get_pos() #transforma x e y na posiçao do clique
        

        x += drone.F_angular(aceleracao, fi)
        
        y = y_force + y
        y += drone.gravity()        
        print(str(y_force) + ' ' + str(np.degrees(fi))) 
        #-----------Limites do Mapa-------------------#
        if y <= 10: y = 10
        elif y >= 435: y = 435

        if x <= 10: x = 10
        elif x >= 890: x = 890
        #---------------------------------------------#

        pygame.display.update()

