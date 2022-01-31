"""

"""
import pygame as pg
from .Tools import States

class Game(States):
    
    
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'

    def cleanup(self):
        print('cleaning up Game state stuff')

    def startup(self):
        print('starting Game state stuff')

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN:
            self.done = True

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((0,0,255))

        