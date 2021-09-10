import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

lightblue = (0,0,130)
Cyan = (62,209,184)
Blue = (15,31,52)
Red = (120,0,0)
Greed = (0, 120,0)

screensize = (700, 500)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Pong Game")

PlayerA = Paddle(Cyan, 10, 100)
PlayerA.rect.x = 20
PlayerA.rect.y = 200

PlayerB = Paddle(Cyan, 10, 100)
PlayerB.rect.x = 670
PlayerB.rect.y = 200

ball = Ball(Cyan, 30, 30)
ball.rect.x = 345
ball.rect.y = 195

all_sprites = pygame.sprite.Group()

all_sprites.add(PlayerA)
all_sprites.add(PlayerB)
all_sprites.add(ball)

loop = True
clock = pygame.time.Clock()

aScore = 0
bScore = 0

# Untill the loop bool is true the main loop will run
while loop:

    for event in pygame.event.get():
        #If the player quit
        if event.type == pygame.QUIT:
            loop = False

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                loop = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        PlayerA.goUp(5)
    if key[pygame.K_s]:
        PlayerA.goDown(5)
    if key[pygame.K_UP]:
        PlayerB.goUp(5)
    if key[pygame.K_DOWN]:
        PlayerB.goDown(5)

    all_sprites.update()

    if ball.rect.x>=690:
        bScore-=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        aScore-=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<60:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, PlayerA) or pygame.sprite.collide_mask(ball, PlayerB):
        ball.bounce()

    screen.fill(Blue)
    pygame.draw.line(screen, Cyan, [349, 0], [349, 500], 5)
    pygame.draw.line(screen, Cyan, [0, 60], [700, 60], 7)

    all_sprites.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(aScore), 1, Cyan)
    screen.blit(text, (250,10))
    text = font.render(str(bScore), 1, Cyan)
    screen.blit(text, (420,10))

    pygame.display.flip()
    clock.tick(40)

pygame.quit()

 
