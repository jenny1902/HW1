import pygame,random
y = 50


#顏色設定
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

#遊戲初始化
pygame.init()

#視窗設定
size = (400,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('1234')

#視窗關閉開關
done = False

clock = pygame.time.Clock()

while not done:
    #有無關視窗
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    #背景顏色
    screen.fill(BLACK)
    
    #主要程式碼
    
for i in range(50):      
   x = random.randint(50, 350)  
   for j in range(200):
        pygame.draw.circle(screen,WHITE,(x,y),5,1)
    
        pygame.display.flip()

        clock.tick(1)
     
        pygame.init()
     
        y = y + 1

pygame.quit()
