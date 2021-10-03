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
        v=self.m*accelerate*np.sin(fi)*2
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
    control = pygame.image.load(r"Images/control.png")
    analog = pygame.image.load(r"Images/analog button.png")
    pygame.mouse.set_visible(1) #mouse invisivel 
    pygame.display.set_caption('Drone Simulator')
    pygame.display.flip()
    
    delta = (0,0)
    autonomo =False
    pi = np.pi
    x_limit= 50, 450
    y_limit= 435, -890 
    y_force = 0
    fi = pi/2
    aceleracao = 0
    x = 500
    y = 435
    y1= 0
    x1 = 0
    erro = (0,0)
    drone = Drone()

    running = True
    while running:
        clock.tick(60)
        screen.blit(bg, (0,0))
        screen.blit(pygame.transform.rotate(ship, -np.degrees(fi)), (x, y))
        screen.blit(control, (50,400))
        screen.blit(analog, (78,(-aceleracao*0.6)+480))
        screen.blit(analog, ((fi*10)+185,480))
        key = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        screen.blit(pointerImg, (pos[0]-15,pos[1]-27))
        

        for event in pygame.event.get(): #procura um evento
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]: #se o evento for do tipo quit
                running = False #fecha o looping
                pygame.display.quit() #fecha o game
                sys.exit() #fecha o sistema


        #------------Comando Horizontal------------------#
        if key[pygame.K_LEFT]: #se clicar pra esquerda
            fi -= pi/180  #decresce a posiçaõ no eixo horizontal para o sentido da direita
        elif key[pygame.K_RIGHT]: #se clicar para direita
            fi += pi/180 #incrementa a posição no eixo horizontal para o sentido da esquerda
            
        #------------Comando Vertical---------------#
        if key[pygame.K_UP]: #se clicar pra cima
            aceleracao += 0.5#decresce a posição no eixo vertical para cima
        elif key[pygame.K_DOWN]: #se clicar para baixo
            aceleracao -= 0.5 #decresce a posiçaõ no eixo vertical para baixo
        
        #------------Comando Waypoint-----------------#
        if event.type == MOUSEBUTTONDOWN: #se o evento for clique do mouse
            x1,y1 = pygame.mouse.get_pos() #transforma x e y na posiçao do clique
            autonomo = True
            aceleracao = -(y1-y)
            
            
        erro = (x1-x, y-y1)  
        if autonomo == True:
            fi -= np.tan((y1-y)/(x1-x))/150
            aceleracao -= (y1-y)/50
            delta = (x1-x,y-y1)


        if fi<=pi/4: fi=pi/4
        elif fi>=3*pi/4: fi=3*pi/4

        if aceleracao>=10: aceleracao=10
        elif aceleracao<=-10: aceleracao=-10

        x += drone.F_angular(aceleracao, fi)
        y_force = drone.F_motor1(aceleracao,fi)
        y = y_force + y
        y += drone.gravity()        
        
        #print(str(y_force) + ' ' + str(np.degrees(fi))) 
        print(str()) 

        #-----------Limites do Mapa-------------------#
        if y <= 0: y = 0
        elif y >= 420: y = 420

        if x <= 0: x = 0
        elif x >= 800: x = 800
        #---------------------------------------------#

        pygame.display.update()

