import pygame
import random
import time

WIDTH, HEIGHT = 600,600
BG = (255,255,255)
BLACK=(0,0,0)

FPS=60

GAME = pygame.display.set_mode((WIDTH,HEIGHT))

BACK = pygame.image.load("Assets/Boards/board3.jpeg")
BACK = pygame.transform.scale(BACK,(WIDTH,HEIGHT))

BLUE = pygame.image.load("Assets/Pieces/blue.png")
BLUE = pygame.transform.scale(BLUE,(40,40))

GREEN = pygame.image.load("Assets/Pieces/green.png")
GREEN = pygame.transform.scale(GREEN,(40,40))

RED = pygame.image.load("Assets/Pieces/red.png")
RED = pygame.transform.scale(RED,(40,40))

YELLOW = pygame.image.load("Assets/Pieces/yellow.png")
YELLOW = pygame.transform.scale(YELLOW,(40,40))

DOTS=[RED,YELLOW,BLUE,GREEN]

def draw(dots):
    GAME.blit(BACK,(0,0))
    for i in range(0,len(dots),1):
        for j in dots[i]:
            GAME.blit(DOTS[i],(j.x,j.y))
            # print(j.x)
    pygame.display.update()
def sett(red):
    red[0].x=red[1].x=red[1].y=red[3].y=61
    red[0].y=red[2].x=red[2].y=red[3].x=141
    

def set_yellow(yellow):
    sett(yellow)
    for i in yellow:
        i.x=561-i.x
        i.y=561-i.y

def set_blue(blue):
    sett(blue)
    for i in blue:
        i.x=561-i.x

def set_green(green):
    sett(green)
    for i in green:
        i.y=561-i.y

def set(dots):
    sett(dots[0])
    set_yellow(dots[1])
    if(len(dots)>2):
        set_blue(dots[2])
    if(len(dots)>3):
        set_green(dots[3])

    
    

def main():
    running = True
    clock = pygame.time.Clock()
    # num=int(input("Number of players (2 to 4): "))
    num=4
    # clock.tick(0)
    dots=[]
    for i in range(num):
        dots.append([pygame.Rect(0,0,40,40),pygame.Rect(0,0,40,40),pygame.Rect(0,0,40,40),pygame.Rect(0,0,40,40)])
    set(dots)
    print(dots)
    GAME.fill(BG)
    while running:

        clock.tick(0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                pass

        keypress = pygame.key.get_pressed()
        draw(dots)
    pygame.quit()

if __name__ == '__main__':
    main()