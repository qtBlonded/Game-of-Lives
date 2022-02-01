"""

"""
import pygame as pg
import sys
from ..components.Grid import Grid
from ..components.Tools import States
from ..components.debug import debug

cells = [
    (1, 5, 5),
    (1, 5, 6),
    (1, 5, 7),
    (1, 6, 5),
    
    (1, 4, 14),
    (1, 5, 14),
    (1, 6, 14),
    (1, 5, 15)
]

glider_gun = [
    (1, 5, 1), (1, 5, 2),  (1, 6, 1), (1, 6, 2),
    (1, 2, 35), (1, 2, 36), (1, 3, 35), (1, 3, 35), 
    (1, 5, 11), (1, 6, 11), (1, 7, 11),
    (1, 4, 12), (1, 8, 12), 
    (1, 3, 13), (1, 9, 13),
    (1, 3, 14), (1, 9, 14),  
    (1, 6, 15),
    (1, 4, 16), (1, 8, 16), 
    (1, 5, 17), (1, 6, 17), (1, 7, 17),
    (1, 6, 18),
    (1, 3, 21), (1, 4, 21), (1, 5, 21),
    (1, 3, 22), (1, 4, 22), (1, 5, 22),
    (1, 2, 23), (1, 6, 23),
    (1, 1, 25), (1, 2, 25), (1, 6, 25), (1, 7, 25) 
]

class Game(States):
    
    
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
        self.col = 40
        self.row = 20
        self.block_size = 30
        self.play_width = self.col * self.block_size
        self.play_height = self.row * self.block_size
        display_rect = pg.display.get_surface().get_rect()
        self.s_width, self.s_height = display_rect.width, display_rect.height
        
        self.top_left_x = (self.s_width - self.play_width) // 2
        self.top_left_y = 50
        self.game_steps = 500
        self.cur_step = 0
        self.delay = 0.100  #delay per step in s


    def cleanup(self):
        print('cleaning up Game state stuff')
        self.cur_step = 0

    def startup(self):
        print('starting Game state stuff')
        pg.display.get_surface().fill((255, 255, 255))
        pg.display.update()
        self.grid = Grid(rows=self.row, cols=self.col)
        for cell in glider_gun:
                self.grid.insert(cell)
        self.time = 0



    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN:
            self.done = True

    def update(self, screen, dt):
        if self.cur_step == self.game_steps:
            self.done = True
        if self.time >= self.cur_step * self.delay:
            self.update_cells(screen)
            #erase_text(window)     
            #draw_text('Current step: ' + str(step), 35, (0, 0, 0), window)
            pg.display.update()
            self.grid.next_step()
            #pygame.time.wait(100)
            self.cur_step += 1
        self.time += dt
        debug(str(self.cur_step) + "  " + str(self.time))

    def draw(self, screen):
        screen.fill((0,0,255))

    def update_cells(self, screen):
        live_color = (0, 0, 0)
        dead_color = (255, 255, 255)
        for row in range(len(self.grid.grid)):  # Swap col and row because of pygame
            for col in range(len(self.grid.grid[0])):
                if self.grid.grid[row][col] > 0:
                    self.draw_cell(screen, row, col, live_color)
                else:
                    self.draw_cell(screen, row, col, dead_color)
        self.draw_grid(screen)

    # draws the lines of the grid for the game
    def draw_grid(self, screen):
        r = g = b = 0
        grid_color = (r, g, b)

        for i in range(self.row + 1):
            # draw grey horizontal lines
            pg.draw.line(screen, grid_color, (self.top_left_x, self.top_left_y + i * self.block_size),
                            (self.top_left_x + self.play_width, self.top_left_y + i * self.block_size))
            for j in range(self.col + 1):
                # draw grey vertical lines
                pg.draw.line(screen, grid_color, (self.top_left_x + j * self.block_size, self.top_left_y),
                                (self.top_left_x + j * self.block_size, self.top_left_y + self.play_height))

    def draw_cell(self, screen, row, col, cell_color):
        cell_rect = pg.Rect(self.top_left_x + col*self.block_size,
                                    self.top_left_y + row*self.block_size, 30, 30)
        pg.draw.rect(screen, cell_color, cell_rect)
"""
def draw_text(text, size, text_color, window):
    pygame.font.init()
    font = pygame.font.SysFont("Arial", size)
    window.blit(font.render(text, False, text_color), (0, 0))

def erase_text(window):
    pygame.draw.rect(window, (255, 255, 255), 
                     pygame.Rect(0, 0, s_width, 50))
    pygame.display.update()

def main_menu(window):
    run = True
    while run:
        draw_text('Press any key to begin', 35, (0, 0, 0), window)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                main(window)
    pygame.quit()
"""
