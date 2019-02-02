import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, color, Width, Height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Width, Height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
