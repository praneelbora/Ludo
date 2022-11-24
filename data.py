import pygame
SIDE=600

start_loc=(((61,141),(141,141),(61,61),(141,61)),((500,420),(420,420),(500,500),(420,500)),((141,500),(141,420),(61,500),(61,420)),((420,61),(420,141),(500,61),(500,141)))
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
start_pos=((40,240),(520,320),(240,520),(320,40))
position=((1,6),(2,6),(3,6),(4,6),(5,6),(6,5),(6,4),(6,3),(6,2),(6,1),(6,0),(7,0),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(9,6),(10,6),(11,6),(12,6),(13,6),(14,6),(14,7),(14,8),(13,8),(12,8),(11,8),(10,8),(9,8),(8,9),(8,10),(8,11),(8,12),(8,13),(8,14),(7,14),(6,14),(6,13),(6,12),(6,11),(6,10),(6,9),(5,8),(4,8),(3,8),(2,8),(1,8),(0,8),(0,7),(0,6))


DOTS=[[]]
RED = pygame.image.load("Assets/Pieces/Red/red1.png")
RED = pygame.transform.scale(RED,(SIDE/15,SIDE/15))
DOTS[0].append(RED)
RED = pygame.image.load("Assets/Pieces/Red/red2.png")
RED = pygame.transform.scale(RED,(SIDE/15,SIDE/15))
DOTS[0].append(RED)
RED = pygame.image.load("Assets/Pieces/Red/red3.png")
RED = pygame.transform.scale(RED,(SIDE/15,SIDE/15))
DOTS[0].append(RED)
RED = pygame.image.load("Assets/Pieces/Red/red4.png")
RED = pygame.transform.scale(RED,(SIDE/15,SIDE/15))
DOTS[0].append(RED)

DOTS.append([])
YELLOW = pygame.image.load("Assets/Pieces/Yellow/yellow1.png")
YELLOW = pygame.transform.scale(YELLOW,(SIDE/15,SIDE/15))
DOTS[1].append(YELLOW)
YELLOW = pygame.image.load("Assets/Pieces/Yellow/yellow2.png")
YELLOW = pygame.transform.scale(YELLOW,(SIDE/15,SIDE/15))
DOTS[1].append(YELLOW)
YELLOW = pygame.image.load("Assets/Pieces/Yellow/yellow3.png")
YELLOW = pygame.transform.scale(YELLOW,(SIDE/15,SIDE/15))
DOTS[1].append(YELLOW)
YELLOW = pygame.image.load("Assets/Pieces/Yellow/yellow4.png")
YELLOW = pygame.transform.scale(YELLOW,(SIDE/15,SIDE/15))
DOTS[1].append(YELLOW)

DOTS.append([])
BLUE = pygame.image.load("Assets/Pieces/Blue/blue1.png")
BLUE = pygame.transform.scale(BLUE,(SIDE/15,SIDE/15))
DOTS[2].append(BLUE)
BLUE = pygame.image.load("Assets/Pieces/Blue/blue2.png")
BLUE = pygame.transform.scale(BLUE,(SIDE/15,SIDE/15))
DOTS[2].append(BLUE)
BLUE = pygame.image.load("Assets/Pieces/Blue/blue3.png")
BLUE = pygame.transform.scale(BLUE,(SIDE/15,SIDE/15))
DOTS[2].append(BLUE)
BLUE = pygame.image.load("Assets/Pieces/Blue/blue4.png")
BLUE = pygame.transform.scale(BLUE,(SIDE/15,SIDE/15))
DOTS[2].append(BLUE)

DOTS.append([])
GREEN = pygame.image.load("Assets/Pieces/Green/green1.png")
GREEN = pygame.transform.scale(GREEN,(SIDE/15,SIDE/15))
DOTS[3].append(GREEN)
GREEN = pygame.image.load("Assets/Pieces/Green/green2.png")
GREEN = pygame.transform.scale(GREEN,(SIDE/15,SIDE/15))
DOTS[3].append(GREEN)
GREEN = pygame.image.load("Assets/Pieces/Green/green3.png")
GREEN = pygame.transform.scale(GREEN,(SIDE/15,SIDE/15))
DOTS[3].append(GREEN)
GREEN = pygame.image.load("Assets/Pieces/Green/green4.png")
GREEN = pygame.transform.scale(GREEN,(SIDE/15,SIDE/15))
DOTS[3].append(GREEN)



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
    if(len(dots)>1):
        set_yellow(dots[1])
    if(len(dots)>2):
        set_blue(dots[2])
    if(len(dots)>3):
        set_green(dots[3])
