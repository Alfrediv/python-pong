import pygame
pygame.init()
screen=pygame.display.set_mode((700,500))
pygame.display.set_caption("PONg")


doExit = False
p1x = 20
p1y = 200
p2x = 680
p2y = 200
p1score=0
p2score=0
clock = pygame.time.Clock()
#ballz variables
bx = 350 #xposition
by = 250 #yposition
bVx = 5 #x velocity horozontal speed 
bVy = 5 #y velocity vertical speed 


while not doExit:#game loop

    # event queue stuff 
    clock.tick(60) #set the fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              doExit = True 

         #game logic here 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_s]:
        p1y+=5

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p2y-=5
    if keys[pygame.K_DOWN]:
        p2y+=5
   # ball movement 
    bx += bVx
    by += bVy

    #reflect ball off side walls of screen,CHANGE SCORE
    if p1y <= 0:
        p1y = 0
    if p1y >= 500:
        p1y = 600
    
    if p2y <= 0:
        p2y = 0
    
    if bx < 0 or bx >= 700: 
        bVx *= -1
    if by <= 0 or by >= 500:
        bVy *= -1
    if bx <= 0: 
        bVx *= -1
        p2score += 1
    elif bx >= 680:
        bVx *= -1
        p1score += 1

    #ball paddle reflection 
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
    #
    if bx >= p2x - 10 and by + 20 > p2y and by < p2y + 100:
        bVx *= -1






    #render section here 
    screen.fill ((0,0,0)) #wipe screen black
    # draw a rectangle
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100), 1)
    pygame.draw.circle(screen, (255,255,255), (bx, by),20)

    #draw a line down the middle
    pygame.draw.line(screen, (255, 255, 255), [349, 0], [349, 500], 5)
     #display scores 
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1score), 1, (255, 255, 255))
    screen.blit(text, (250,10))
    text = font.render(str(p2score), 1, (255, 255, 255))
    screen.blit(text, (420,10))

    #update the screen 
    pygame.display.flip()
   



#End game loop
pygame.quit()

  