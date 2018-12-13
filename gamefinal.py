import pygame
import random
pygame.init()
displaysize=725
playersize=25 #for good see displaysize//playersize is odd
surface=pygame.display.set_mode((displaysize,displaysize))
surface.fill((0,0,0))
bots=[]
motion=0
clock=pygame.time.Clock()
frames=15
bombtime=45
firingtime=30
numberofbombsused=0
numberofbotskilled=0
numberofbot=displaysize//playersize#4
numberoftimeskilledbybot=0
class player:
    def __init__(self,color):
        self.motion=0
        self.color=color
        self.position=[0,0]
player1=player((0,0,255))
for _ in range(numberofbot):
    bots.append(player((0,255,0)))
    bots[_].position=[0,displaysize-playersize]
def checkposition(x):
    if not (x[0]>=0 and x[0]<=displaysize-playersize and x[1]>=0 and x[1]<=displaysize-playersize):
        return(0)
    if x in gridlist:
        return(0)
    if x in [i[0:2] for i in bomblist]:
        return(0)
    return(1)

def updateall():
    for i in bots:
        pygame.draw.rect(surface,i.color,i.position+[playersize,playersize])
    for fire in range(len(firinglist)):
        firinglist[fire][2]-=1
        pygame.draw.rect(surface,(225,0,0),[firinglist[fire][0],firinglist[fire][1],playersize,playersize])
        if firinglist[fire][2]<=0:
            fillblack(firinglist.pop(fire)[0:2])
            break
    pygame.draw.rect(surface, player1.color, player1.position + [playersize, playersize])
    pygame.display.update()

def fillblack(x):
    pygame.draw.rect(surface,(0,0,0),x+[playersize,playersize])


gridlist=[]
for i in range(displaysize//playersize):
    for j in range(displaysize//playersize):
        gridlist.append([i*2*playersize+playersize,j*2*playersize+playersize])
        pygame.draw.rect(surface,(255,255,255),[i*2*playersize+playersize,j*2*playersize+playersize,playersize,playersize])
bomblist=[]
firinglist=[]
while(1):
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            print("bombs used   ",numberofbombsused)
            print("bots killed  ",numberofbotskilled)
            print("killed by bot",numberoftimeskilledbybot)
            pygame.quit()
            quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_w:
                player1.motion=1
            if i.key==pygame.K_s:
                player1.motion=3
            if i.key==pygame.K_a:
                player1.motion=4
            if i.key==pygame.K_d:
                player1.motion=2
            if i.key==pygame.K_SPACE:
                bomblist =bomblist+[[p for p in player1.position +[bombtime]]]
                numberofbombsused+=1
        if i.type==pygame.KEYUP:
            if i.key in [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d]:
                player1.motion=0
    for bot in bots:
        bot.motion=max(random.randint(-2,4),0)#changethisto (-4,4)
        if bot.position in [i[0:2] for i in firinglist]:
            numberofbotskilled+=1
            bot.position=[0,displaysize-playersize]
        if bot.position==player1.position:
            numberoftimeskilledbybot+=1
            player1.position=[0,0]
    for bomb in range(len(bomblist)):
        fillblack(bomblist[bomb][0:2])
        pygame.draw.circle(surface,(255,255,0),(bomblist[bomb][0]+playersize//2,bomblist[bomb][1]+playersize//2),(((bomblist[bomb][2])//(bombtime//3)))*playersize//6)
        if bomblist[bomb][2]<=0:
            fillblack(bomblist[bomb][0:2])
            bombpositionx,bombpositiony=bomblist.pop(bomb)[0:2]
            firinglist.append([bombpositionx, bombpositiony] + [firingtime])
            if checkposition([bombpositionx+playersize,bombpositiony]):
                firinglist.append([bombpositionx+playersize,bombpositiony]+[firingtime])
            if checkposition([bombpositionx-playersize,bombpositiony]):
                firinglist.append([bombpositionx-playersize,bombpositiony]+[firingtime])
            if checkposition([bombpositionx,bombpositiony+playersize]):
                firinglist.append([bombpositionx,bombpositiony+playersize]+[firingtime])
            if checkposition([bombpositionx,bombpositiony-playersize]):
                firinglist.append([bombpositionx,bombpositiony-playersize]+[firingtime])
            break
        bomblist[bomb][2]-=1
    for man in [player1]+bots:
        if man.motion==1:
            if checkposition([man.position[0],man.position[1]-playersize]):
                fillblack([man.position[0],man.position[1]])
                man.position[1]=man.position[1]-playersize
        if man.motion==3:
            if checkposition([man.position[0], man.position[1] + playersize]):
                fillblack([man.position[0], man.position[1]])
                man.position[1]=man.position[1]+playersize
        if man.motion==2:
            if checkposition([man.position[0]+playersize,man.position[1]]):
                fillblack([man.position[0], man.position[1]])
                man.position[0]=man.position[0]+playersize
        if man.motion==4:
            if checkposition([man.position[0]-playersize, man.position[1]]):
                fillblack([man.position[0], man.position[1]])
                man.position[0]=man.position[0]-playersize
    updateall()
    clock.tick(frames)