"""
This starts the pygame window to begin a game of "Game of Lives".

Author: Quinn Bardwell
Date: 01-29-22
"""

import pygame
from Grid import Grid

if __name__ == "__main__":
    grid = Grid()
    grid.grid_print()

    cells = [
        (1, 5, 5),
        (1, 5, 6),
        (1, 5, 7),
        (1, 6, 5)
    ]
    for cell in cells:
        grid.insert(cell)

    grid.grid_print()