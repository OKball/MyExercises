
import pygame

WIN_WIDTH = 900
WIN_HEIGHT = 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
REFRESH_RATE = 60
SCREEN_CENTER = WIN_WIDTH / 2 , WIN_HEIGHT / 2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.display.set_caption("Skaczący kwadracik")

def main():
    RUN = True
    CLOCK = pygame.time.Clock()
    rectangle = pygame.rect.Rect(450 ,400 ,50 ,50)
    rectangle_draging = False
    color = RED
    timer = 0
    VELOCITY = -200
    while RUN:
        CLOCK.tick(REFRESH_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    if rectangle.collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle.x - mouse_x
                        offset_y = rectangle.y - mouse_y
                        VELOCITY = 0

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    rectangle_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if rectangle_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle.x = mouse_x + offset_x
                    rectangle.y = mouse_y + offset_y
                    
        if rectangle_draging == True:
            color = ((int(timer/3) + 200)%100 + 100, (int(timer/2))%100 + 100, (int(timer/5))%100 + 100) 
            timer += 2   

        if rectangle_draging == False:    
            GRAVITYFORCE = 4
            if rectangle.y == WIN_HEIGHT - rectangle.h:
                GRAVITYFORCE = 0
            if rectangle.y > WIN_HEIGHT - rectangle.h:
                rectangle.y = WIN_HEIGHT - rectangle.h
                VELOCITY = round(VELOCITY / 2) * -1
            VELOCITY = VELOCITY + GRAVITYFORCE   
            rectangle.y = rectangle.y + int(VELOCITY / 10)

        WIN.fill(BLACK)
        pygame.draw.rect(WIN, color, rectangle)
        pygame.display.update()


    


if __name__ == "__main__":
    main()