import pygame
pygame.init()
from functools import reduce

level = {
    "title" : 'LEVEL 1',
    "size_x" : 7,
    "size_y" : 7,
    "player_x" : 3,
    "player_y" : 4,
    "destination_pos" : [(2,2),(3,3),(4,3)],
    "box_pos" :  [(2,3),(2,4),(3,2)],
    "wall_pos" : [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(1,6),(2,6),(3,6),(4,6),(5,6)],
    "componunt_size" : 50
}

title = level["title"]
size_x = level["size_x"]
size_y = level["size_y"]
player_x = level["player_x"]
player_y = level['player_y']
destination_pos = level["destination_pos"]
box_pos = level["box_pos"]
wall_pos = level["wall_pos"]
componunt_size = level["componunt_size"]

screen = pygame.display.set_mode((componunt_size*size_x,componunt_size*size_y))
pygame.display.set_caption(title)  
run = True

wall_img = pygame.transform.scale(pygame.image.load("wall.png"), (componunt_size,componunt_size))
player_img = pygame.transform.scale(pygame.image.load("mario.png"), (componunt_size,componunt_size))
destination_img = pygame.transform.scale(pygame.image.load("destination.png"), (componunt_size,componunt_size))
box_img = pygame.transform.scale(pygame.image.load("box.png"), (componunt_size,componunt_size))

home_img = pygame.transform.scale(pygame.image.load("home.png"), (200,70))
# next_img = pygame.transform.scale(pygame.image.load("next.png"), (200,70))
close_img = pygame.transform.scale(pygame.image.load("close.png"), (200,70))




def draw_img_at(x,y,img):
    screen.blit(img, (y*componunt_size,x*componunt_size))

def draw_componunt(componunt_img,compnunt_list):
    for pos in compnunt_list:
        draw_img_at(pos[0],pos[1],componunt_img)

winner_flag = False
def chacker_winner():
    global winner_flag,screen
    res = reduce(lambda x, y: x+box_pos.count(y), set(destination_pos), 0)
    if(res == len(destination_pos)):
        print("winnner....")

        winner_flag = True
        screen=pygame.display.set_mode((240,300))

while(run):
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if (event.type == pygame.KEYDOWN and winner_flag==False):

            if event.key == pygame.K_UP:

                if((player_x-1,player_y) not in box_pos and (player_x-1,player_y) not in wall_pos):
                    player_x = player_x -1 

                elif((player_x-1,player_y) in box_pos and (player_x-2,player_y) not in box_pos and (player_x-2,player_y) not in wall_pos):
                    box_pos[box_pos.index((player_x-1,player_y))] = (player_x-2,player_y)
                    player_x = player_x -1 



            elif event.key == pygame.K_DOWN:

                if((player_x+1,player_y) not in box_pos and (player_x+1,player_y) not in wall_pos):
                    player_x = player_x + 1

                elif((player_x+1,player_y) in box_pos and (player_x+2,player_y) not in box_pos and (player_x+2,player_y) not in wall_pos):
                    box_pos[box_pos.index((player_x+1,player_y))] = (player_x+2,player_y)
                    player_x = player_x + 1 


            elif event.key == pygame.K_LEFT:

                if((player_x,player_y-1) not in box_pos and (player_x,player_y-1) not in wall_pos):
                    player_y = player_y - 1

                elif((player_x,player_y-1) in box_pos and (player_x,player_y-2) not in box_pos and (player_x,player_y-2) not in wall_pos):
                    box_pos[box_pos.index((player_x,player_y-1))] = (player_x,player_y-2)
                    player_y = player_y - 1

            elif event.key == pygame.K_RIGHT:

                if((player_x,player_y+1) not in box_pos and (player_x,player_y+1) not in wall_pos ):
                    player_y = player_y + 1

                elif((player_x,player_y+1) in box_pos and (player_x,player_y+2) not in box_pos and (player_x,player_y+2) not in wall_pos):
                    box_pos[box_pos.index((player_x,player_y+1))] = (player_x,player_y+2)
                    player_y = player_y + 1


    if(winner_flag==False):
        draw_img_at(player_x,player_y,player_img)
        draw_componunt(wall_img,wall_pos)
        draw_componunt(box_img,box_pos)
        draw_componunt(destination_img,destination_pos)
        chacker_winner()

    if(winner_flag==True):
        mouse = pygame.mouse.get_pos()
        screen.blit(home_img,(20,20))
        screen.blit(close_img,(20,200))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(mouse[0]>=20 and mouse[0]<=220 and mouse[1]>=20 and mouse[1]<=90):
                print("home no event add..")
            elif(mouse[0]>=20 and mouse[0]<=220 and mouse[1]>=200 and mouse[1]<=270):
                run = False
            print(mouse)
                

    pygame.display.flip()