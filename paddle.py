import pygame
Blue = (15,31,52)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(Blue)
        self.image.set_colorkey(Blue)

        pygame.draw.rect(self.image, color, [0,0, width, height])

        self.rect = self.image.get_rect()


    def goUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 60:
            self.rect.y = 60

    def goDown(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 400:
            self.rect.y = 400


    
