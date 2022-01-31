"""

"""
import pygame as pg
from .Tools import States
from .Tools import MenuManager


class Menu(States, MenuManager):
    
    
    def __init__(self):
        States.__init__(self)
        MenuManager.__init__(self)
        self.next = 'game'
        self.options = ['Play', 'Options', 'Quit']
        self.next_list = ['game', 'options']
        self.pre_render_options()
        self.from_bottom = 200
        self.spacer = 75

    def cleanup(self):
        print('cleaning up Main Menu state stuff')

    def startup(self):
        print('starting Main Menu state stuff')

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        self.get_event_menu(event)

    def update(self, screen, dt):
        self.update_menu()
        self.draw(screen)

    def draw(self, screen):
        screen.fill((255,0,0))
        self.draw_menu(screen)

        