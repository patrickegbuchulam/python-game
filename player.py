import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("runner1.gif").convert_alpha()
        #self.image = pygame.Surface([50, 50])
        #self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (50, 300)
        self.in_air = False
        self.ticker=15
        
    def set_pos(self, x, y):
        self.rect.x, self.rect.y = x, y

    def get_loc(self):
        return self.loc

    def jump(self):
        if self.in_air == False:
            self.set_pos(self.rect.x, self.rect.y-50)
        else:
            pass
        self.in_air = True

    def reset(self):
        self.set_pos(50,300)

    def tick(self):
        self.ticker-=1
        if self.ticker<=0:
            self.reset()
            self.in_air = False
            self.ticker=15

    def set_jump_time(self, time):
        if self.ticker!=8:
            self.ticker=time


