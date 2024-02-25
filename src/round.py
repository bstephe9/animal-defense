import pygame as pg

class Round():
    def __init__(self):
        self.score = 0
        self.gold = 500
        
        self.screen = pg.display.get_surface()
        self.background = pg.image.load(
            r"data/backgrounds/environment_forestbackground1.png").convert_alpha()
        self.all_sprites = pg.sprite.Group()
            

    def draw(self):
        self.screen.blit(self.background, (0,0))
        pg.display.flip()