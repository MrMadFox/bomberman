import pygame
pygame.init()
playersize=50
bombtime=30
dimentions=[650,650]
s=pygame.display.set_mode(dimentions)
s.fill((0,0,0))
pygame.display.update()
clock=pygame.time.Clock()
import random
class player:
    def __init__(self):
        self.position=[0,0]
    def update(self):
        pygame.draw.rect(s,(0,0,255),(self.position[0],self.position[1],playersize,playersize))
player1=player()
bots=[]
for i in range(1):
    bots.append(player())
player2=player()
def updateall():
    s.fill((0,0,0))
    player1.update()
    for bombs in range(len(bomblist)):
        pygame.draw.circle(s,(0,225,0),(bomblist[bombs][0]+playersize//2,bomblist[bombs][1]+playersize//2),bomblist[bombs][2])
        if bomblist[bombs][2]==0:
            blasting.append(bomblist.pop(bombs)[0:2]+[150])
            break
        else:
            bomblist[bombs][2]=bomblist[bombs][2]-1
    for i in bots:
        i.update()

    for blast in range(len((blasting))):
        blasting[blast][2]=blasting[blast][2]-10
        if blasting[blast][2]==0:
            blasting.pop(blast)
            break
        if blasting[blast]!=0:
            pygame.draw.rect(s, (255, 0, 0), (blasting[blast][0],blasting[blast][1], playersize, playersize))
            if blasting[blast][0]>playersize:
                #left
                pygame.draw.rect(s, (255, 0, 0), (blasting[blast][0]-playersize, blasting[blast][1], playersize, playersize))
            if blasting[blast][0]<dimentions[0]-2*playersize:
                #right
                pygame.draw.rect(s, (255, 0, 0), (blasting[blast][0]+playersize, blasting[blast][1], playersize, playersize))
            if blasting[blast][1]>playersize:
                #top
                pygame.draw.rect(s, (255, 0, 0), (blasting[blast][0], blasting[blast][1]-playersize, playersize, playersize))
            if blasting[blast][1]<dimentions[1]-2*playersize:
                #down
                pygame.draw.rect(s, (255, 0, 0), (blasting[blast][0], blasting[blast][1]+playersize, playersize, playersize))
    for i in blocks:
        pygame.draw.rect(s, (255, 255, 255), (i[0], i[1], playersize, playersize))
    pygame.display.update()
motion=0
blocks=[]
for i in range(dimentions[0]//100):
    for j in range(dimentions[0]//100):
        blocks.append([50+i*100,50+j*100])
for i in blocks:
    pygame.draw.rect(s,(255,255,255),(i[0],i[1],playersize,playersize))
pygame.display.update()
bomblist=[]
blasting=[]
def checkposition(x):
    if x in blocks:
        return(0)
    return(1)
while(1):
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_w:
                motion=1
            if i.key==pygame.K_s:
                motion=3
            if i.key==pygame.K_a:
                motion=4
            if i.key==pygame.K_d:
                motion=2
            if i.key==pygame.K_SPACE:
                bomblist=bomblist+[[p for p in player1.position +[bombtime]]]
        if i.type==pygame.KEYUP:
            if i.key in [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d]:
                motion=0
    if motion==1:
        if player1.position[1]>0:
            if checkposition([player1.position[0],player1.position[1]-50]):
                player1.position[1]=player1.position[1]-50
    if motion==3:
        if player1.position[1]<dimentions[1]-playersize:
            if checkposition([player1.position[0], player1.position[1] + 50]):
                player1.position[1]=player1.position[1]+50
    if motion==2:
        if player1.position[0]<dimentions[0]-playersize:
            if checkposition([player1.position[0]+50,player1.position[1]]):
                player1.position[0]=player1.position[0]+50
    if motion==4:
        if player1.position[0]>0:
            if checkposition([player1.position[0]-50, player1.position[1]]):
                player1.position[0]=player1.position[0]-50
    for i in bots:
        move=random.randint(1,4)
        if move == 1:
            if i.position[1] > 0:
                if checkposition([i.position[0], i.position[1] - 50]):
                    i.position[1] = i.position[1] - 50
        elif move == 3:
            if i.position[1] < dimentions[1] - playersize:
                if checkposition([i.position[0], i.position[1] + 50]):
                    i.position[1] = i.position[1] + 50
        elif move == 2:
            if i.position[0] < dimentions[0] - playersize:
                if checkposition([i.position[0] + 50, i.position[1]]):
                    i.position[0] = i.position[0] + 50
        else :
            if i.position[0] > 0:
                if checkposition([i.position[0] - 50, i.position[1]]):
                    i.position[0] = i.position[0] - 50


    updateall()
    clock.tick(15)