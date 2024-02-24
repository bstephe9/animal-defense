import os
import pygame as pg

from src.constants import *

class Game:
    def __init__(self):
        # initializes game properties
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        
        # load sprites
        self.background = pg.image.load(r"data/backgrounds/environment_forestbackground1.png")


    def new(self):
        self.show_start_screen()
        self.all_sprites = pg.sprite.Group()
        self.run()
        self.show_game_over_screen()


    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False


    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()


    def show_start_screen(self):
        pass


    def show_game_over_screen(self):
        pass


def main():
    g = Game()
    while g.running:
        g.new()
        g.show_game_over_screen()
        
    pg.quit()
        
        
if __name__ == "__main__":
    main()
