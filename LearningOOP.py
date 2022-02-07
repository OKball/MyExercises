import pygame
import random


WIN_WIDTH = 900
WIN_HEIGHT = 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Glupi kwadrat")
REFRESH_RATE = 60
SCREEN_CENTER = WIN_WIDTH / 2 , WIN_HEIGHT / 2
CLOCK = pygame.time.Clock()



class colors:
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)



class square:
    def __init__(self, X, Y, W, H, C, VELOCITY_Y, VELOCITY_X):
        self.X = X
        self.Y = Y
        self.W = W
        self.H = H
        self.C = C
        self.VELOCITY_Y = VELOCITY_Y
        self.VELOCITY_X = VELOCITY_X
    def physics(self):
        GRAVITYFORCE = 4
        if self.Y == 580:
            GRAVITYFORCE = 0
        if self.Y > 580:
            self.Y = 580
            self.VELOCITY_Y = round(self.VELOCITY_Y / 2) * -1
        self.VELOCITY_Y = self.VELOCITY_Y + GRAVITYFORCE   
        self.Y = self.Y + round(self.VELOCITY_Y / 10)
        if self.X < 0:
            self.X = 0
            self.VELOCITY_X = self.VELOCITY_X * -1
        if self.X > 880:
            self.X = 880
            self.VELOCITY_X = self.VELOCITY_X * -1
        if abs(self.VELOCITY_X) > 0.5:
            if self.Y == 580:
                self.VELOCITY_X = self.VELOCITY_X * 0.98
        else:
            self.VELOCITY_X = 0
        self.X = self.X + self.VELOCITY_X
    def draw(self):
        pygame.draw.rect(WIN, self.C, pygame.Rect(self.X, self.Y, self.W, self.H))
    


def drawBouncingRect():
        pygame.draw.rect(WIN, square.C, pygame.Rect(square.X, square.Y, square.W, square.H))



def drawRect(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT, COLOR):
    pygame.draw.rect(WIN, COLOR, pygame.Rect(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT))



def drawBouncingRect(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT, COLOR):
    pygame.draw.rect(WIN, COLOR, pygame.Rect(RECTANGLE_X, RECTANGLE_Y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT))
    BouncingRectX, BouncingRectY = "", ""
    
    VELOCITY = -200
    GRAVITYFORCE = 4
    if BouncingRectY == 580:
        GRAVITYFORCE = 0
    if BouncingRectY > 580:
        R_Y = 580
        VELOCITY = round(VELOCITY / 2) * -1
    
    VELOCITY = VELOCITY + GRAVITYFORCE   
    R_Y = R_Y + (VELOCITY / 10)



def main():
    RUN = True
    R_X , R_Y = 450, 300
    R_W = 10
    R_H = 10
    VELOCITY_Y = -5
    VELOCITY_X = 2
    lista = []
    while RUN:
        
        CLOCK.tick(REFRESH_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                pygame.quit()
        WIN.fill(colors.black)


        def spawnKwadrat(x):
            for i in range(x):
                kwadrat = square(R_X, R_Y, R_W, R_H, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),), random.randint(-200, -10),  VELOCITY_X * (random.randint(1, 100) / 10))
                lista.append(kwadrat)
                if len(lista) > 3000:
                    del lista[0]     
            print(len(lista))


        if R_Y > 550:
            VELOCITY_Y = VELOCITY_Y * -1
            spawnKwadrat(random.randint(10, 20))
        if R_Y < 0:
            VELOCITY_Y = VELOCITY_Y * -1
            spawnKwadrat(random.randint(10, 20))
        if R_X < 440:
            VELOCITY_X = VELOCITY_X * -1
            spawnKwadrat(random.randint(10, 20))
        if R_X > 460:
            VELOCITY_X = VELOCITY_X * -1
            spawnKwadrat(random.randint(10, 20))

        for i in lista:
            i.physics()
            i.draw()

        R_Y = R_Y + VELOCITY_Y
        R_X = R_X + VELOCITY_X
        drawRect(R_X, R_Y, R_W, R_H, colors.green)
        

        pygame.display.update()


    


if __name__ == "__main__":
    main()