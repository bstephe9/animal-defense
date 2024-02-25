import pygame as pg
import sys

from src.constants import *

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = False
        self.round = None

    def start_round(self):
        self.round = Round()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        self.round.handle_events() 

    def update(self):
        if self.round:
            self.round.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.round:
            self.round.draw()
        pg.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    
class Round:
    def __init__(self):
        # Create groups
        self.towers = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.gui = pg.sprite.Group()
        
        # Background
        self.screen = pg.display.get_surface()
        self.background = pg.image.load(
            r"data/backgrounds/environment_forestbackground1.png").convert_alpha()
        
        # Create towers
        self.tower1 = Tower(0, 50, True, self.towers)
        self.tower2 = Tower(SCREEN_WIDTH-250,50, False, self.towers)

        # Create button to spawn soldiers
        
    def handle_events(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            Enemy(200, SCREEN_HEIGHT-150, True, self.enemies)
            
        
        
        
    def update(self):
        # Update round-specific logic
        self.towers.update()
        self.enemies.update()

    def draw(self):
        # Draw round-specific elements on the screen
        self.screen.blit(self.background, (0,0))
        self.towers.draw(self.screen)
        self.enemies.draw(self.screen)
    

# TODO Create object since there's code reuse

class Tower(pg.sprite.Sprite):
    def __init__(self, x, y, reversed, group=None):
        super().__init__(group)
        self.image = pg.image.load("data/objects/tower.png").convert_alpha() 
        if reversed:
            self.image = pg.transform.flip(self.image, True, False)
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, reversed, group=None):
        super().__init__(group)
        self.image = pg.image.load("data/characters/rpg-beings/Polar bear.png").convert_alpha() 
        if reversed:
            self.image = pg.transform.flip(self.image, True, False)
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.x += 3

if __name__ == "__main__":
    pg.init()
    game = Game()
    game.start_round()  # Start the first round
    game.run()
    pg.quit()
    sys.exit()
    