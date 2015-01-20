import pygame, sys

class player(Pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprint.__init__(self)
        self.image = pygame.image.load("runner1.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (10, 200)
        
    def set_pos(self, x, y):
        self.rect.x, self.rect.y = x, y

    def get_loc(self):
        return self.loc


