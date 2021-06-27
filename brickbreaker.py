import pygame
pygame.init()

WIDTH = 1100
HEIGHT = 580
win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("First Game")
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()

class Ball:    
    def __init__(self,x,y,dx,dy,color):
        self.w = 30
        self.h = 30
        self.img = pygame.transform.scale(pygame.image.load('ball2.png'),(self.w,self.h))
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.score = 0
    def draw(self,win):
        #pygame.draw.circle(win,self.color,(self.x,self.y),25)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        win.blit(self.img,(self.x,self.y))
    def update(self,win,bar,bricks):       

        #Wall Collision
        if self.x + self.w >= WIDTH or self.x <= 0:   #left and right wall  
            self.dx = -self.dx
        if self.y <=0 : #top wall
            self.dy = -self.dy            
        if self.y+self.h >= HEIGHT:   #bottom wall
            self.score = self.score - 2
            self.dy = -self.dy
            
        #BAR COLLISION
        if self.x + self.w > bar.x and self.x+self.w <= bar.x + bar.w and self.y + self.h > bar.y and self.y + self.h < bar.y+bar.h:
            self.dy = -self.dy

        #Bricks Collision
        if self.dx>0 and self.dy<0:
            for i in range(4):
                for j in range(10):
                    if bricks[j+i*10].hit == False:
                        if self.x+ self.w>=bricks[j+i*10].x and self.x+self.w<=bricks[j+i*10].x+bricks[j+i*10].w and self.y>=bricks[j+i*10].y and self.y<=bricks[j+i*10].y+bricks[j+i*10].h:
                            bricks[j+i*10].hit = True
                            self.dy = -self.dy
                            self.score = self.score + 5
        elif self.dx<0 and self.dy<0:
            for i in range(4):
                for j in range(10):
                    if bricks[j+i*10].hit == False:
                        if self.x>=bricks[j+i*10].x and self.x<=bricks[j+i*10].x+bricks[j+i*10].w and self.y>=bricks[j+i*10].y and self.y<=bricks[j+i*10].y+bricks[j+i*10].h:
                            bricks[j+i*10].hit = True
                            self.dy = -self.dy
                            self.score = self.score + 5
        elif self.dx<0 and self.dy>0:
            for i in range(4):
                for j in range(10):
                    if bricks[j+i*10].hit == False:
                        if self.x>=bricks[j+i*10].x and self.x<=bricks[j+i*10].x+bricks[j+i*10].w and self.y+self.h>=bricks[j+i*10].y and self.y+self.h<=bricks[j+i*10].y+bricks[j+i*10].h:
                            bricks[j+i*10].hit = True
                            self.dy = -self.dy
                            self.dx = -self.dx
                            self.score = self.score + 5
        elif self.dx>0 and self.dy>0:
            for i in range(4):
                for j in range(10):
                    if bricks[j+i*10].hit == False:
                        if self.x+ self.w>=bricks[j+i*10].x and self.x+ self.w<=bricks[j+i*10].x+bricks[j+i*10].w and self.y+self.h>=bricks[j+i*10].y and self.y+self.h<=bricks[j+i*10].y+bricks[j+i*10].h:
                            bricks[j+i*10].hit = True
                            self.dy = -self.dy
                            self.dx = -self.dx
                            self.score = self.score + 5
            
        self.draw(win)

class Bar:
    def __init__(self,x,y,dx,color):
        self.w = 200
        self.h = 15
        self.x = x
        self.y = y
        self.dx = dx
        self.color = color
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.w,self.h))
        self.dx = 0
    def update(self,win):
        self.x = self.x + self.dx        
        self.draw(win)

class Brick:
    def __init__(self,x,y,hit):
        self.w = 75
        self.h = 25
        self.img = pygame.transform.scale(pygame.image.load('brick.png'),(self.w,self.h))
        self.x = x
        self.y = y
        self.hit = hit
    def draw(self,win):
         win.blit(self.img,(self.x,self.y))
    def update(self,win):
        self.draw(win)

run = True
space=False
ball = Ball(430,500,2,2,(200,200,20))
bar = Bar(400,550,1,(100,100,200))
BAR_LEN = 70
BAR_WID = 25
hit=False
bricks = []
brick_count=0
for i in range(4):
    for j in range(10):
        x = 100+BAR_LEN*j+20*j
        y = 50+BAR_WID*i+20*i
        brick = Brick(x,y,hit)
        bricks.insert(brick_count,brick)
        brick_count = brick_count + 1
        

def redrawindow(space):
    win.fill((0,0,0))
    bar.update(win)
    if space:
        ball.update(win,bar,bricks)  
    for i in range(4):
        for j in range(10):
            if not bricks[j+i*10].hit:            
                bricks[j+i*10].update(win)            
    count = 'Score: ' +str(ball.score)
    textsurface1 = myfont.render(count, False, (34, 56, 200))
    win.blit(textsurface1,(10,10))
    pygame.display.update()

while run:
    #pygame.time.delay(3)
    #clock.tick(90) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        space = True
        #pygame.event.clear()
    if keys[pygame.K_ESCAPE]:
        space = False
        #pygame.event.clear()
    if keys[pygame.K_LEFT]:
        bar.dx = -5
        #pygame.event.clear()
    if keys[pygame.K_RIGHT]:
        bar.dx = 5
        #pygame.event.clear()
    if keys[pygame.K_a]: #increase height
        bar.h = bar.h+1
        bar.y = bar.y-1
        #pygame.event.clear()
    if keys[pygame.K_s]:    #decrease height
        if bar.h >15:
            bar.h = bar.h-1
            bar.y = bar.y+1 
        #pygame.event.clear()
    redrawindow(space)
        
pygame.quit()