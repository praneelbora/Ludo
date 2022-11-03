import pygame
import random
import time

WIDTH, HEIGHT = 600,600
BG = (255,255,255)
BLACK=(0,0,0)
clock = pygame.time.Clock()

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

in_start=[]
start_loc=(((61,141),(141,141),(61,61),(141,61)),((520,420),(420,420),(500,500),(420,500)),((141,500),(141,420),(61,500),(61,420)),((420,61),(420,141),(500,61),(500,141)))
"""
start location of all pieces
(red_all,yellow_all,blue_all,green_all)
red_all ->      ●(2)    ●(3)
                ●(0)    ●(1)
yellow_all ->   ●(1)    ●(0)
                ●(3)    ●(2)
blue_all ->     ●(3)    ●(1)
                ●(2)    ●(0)
greeen_all ->   ●(0)    ●(2)
                ●(1)    ●(3)

"""
def draw(dots):
    GAME.blit(BACK,(0,0))
    for i in range(0,len(dots),1):
        for j in dots[i]:
            GAME.blit(DOTS[i],(j.x,j.y))
            pygame.display.update()
            clock.tick(10)
            # print(j.x)
    # pygame.display.update()
def rand():
    val=int(random.random()*6)
    return (val if (val>0) else rand())
def sett(piece,a,b,c,d,e,f):
    piece[a].x=piece[a].y=piece[b].x=piece[c].y=61
    piece[b].y=piece[c].x=piece[d].x=piece[d].y=141
    for i in piece:
        if e==1:i.x=561-i.x
        if f==1:i.y=561-i.y

def set_red(red):
    sett(red,2,0,3,1,0,0)
    """ 
    2 gets used for x=61 and y=61
    0 gets used for x=61 and y=141
    3 gets used for x=141 and y=61
    1 gets used for x=141 and y=141
    0 gets used for x shift (0 for no shift, 1 for shift)
    0 gets used for y shift (0 for no shift, 1 for shift)
    """
    
def set_yellow(yellow):
    sett(yellow,2,0,3,1,1,1)

def set_blue(blue):
    sett(blue,2,3,0,1,0,1)
    """ 
    2 gets used for x=61 and y=61 but because of shift, x=61,y=600-61=539
    3 gets used for x=61 and y=141
    0 gets used for x=141 and y=61
    1 gets used for x=141 and y=141
    0 gets used for x shift (0 for no shift, 1 for shift)
    1 gets used for y shift (0 for no shift, 1 for shift)
    """
def set_green(green):
    sett(green,2,3,0,1,1,0)


def set(dots):
    set_red(dots[0])
    set_yellow(dots[1])
    if(len(dots)>2):
        set_blue(dots[2])
    if(len(dots)>3):
        set_green(dots[3])

    

def main():
    running = True
    # num=int(input("Number of players (2 to 4): "))
    num=4
    # clock.tick(0)
    dots=[]
    for i in range(num):
        in_start.append(4)
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