"""
This starts the pygame window to begin a game of "Game of Lives".

Author: Quinn Bardwell
Date: 01-29-22
"""

import pygame
from Grid import Grid
import sys

# global variables
col = 20  # 10 columns
row = 10  # 20 rows
s_width = 800  # window width
s_height = 750  # window height
play_width = 600  # play window width; 600/20 = 30 width per block
play_height = 300  # play window height; 300/10 = 30 height per block
block_size = 30  # size of block

top_left_x = (s_width - play_width) // 2
top_left_y = 50

game_steps = 10

cells = [
    (1, 5, 5),
    (1, 5, 6),
    (1, 5, 7),
    (1, 6, 5)
]

def main(window):
    erase_text(window)
    grid = Grid(rows=row, cols=col)
    for cell in cells:
        grid.insert(cell)

    for step in range(game_steps + 1):  # Account for initial state
        update_cells(window, grid.grid)
        erase_text(window)     
        draw_text('Current step: ' + str(step), 35, (0, 0, 0), window)
        pygame.display.update()
        grid.next_step()
        pygame.time.wait(500)

    erase_text(window)

def update_cells(surface, grid):
    live_color = (0, 0, 0)
    dead_color = (255, 255, 255)
    for row in range(len(grid)):  # Swap col and row because of pygame
        for col in range(len(grid[0])):
            if grid[row][col] > 0:
                draw_cell(surface, row, col, live_color)
            else:
                draw_cell(surface, row, col, dead_color)
    draw_grid(surface)
    pygame.display.update()

# draws the lines of the grid for the game
def draw_grid(surface):
    r = g = b = 0
    grid_color = (r, g, b)

    for i in range(row + 1):
        # draw grey horizontal lines
        pygame.draw.line(surface, grid_color, (top_left_x, top_left_y + i * block_size),
                         (top_left_x + play_width, top_left_y + i * block_size))
        for j in range(col + 1):
            # draw grey vertical lines
            pygame.draw.line(surface, grid_color, (top_left_x + j * block_size, top_left_y),
                             (top_left_x + j * block_size, top_left_y + play_height))

def draw_cell(surface, row, col, cell_color):
    cell_rect = pygame.Rect(top_left_x + row*block_size,
                                 top_left_y + col*block_size, 30, 30)
    pygame.draw.rect(surface, cell_color, cell_rect)

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


if __name__ == '__main__':
    window = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Game of Lives')

    # Paint background of the screen
    pygame.draw.rect(window, (255, 255, 255), 
                     pygame.Rect(0, 0, s_width, s_height))

    main_menu(window)