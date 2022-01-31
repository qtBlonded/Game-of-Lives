"""
This starts the pygame window to begin a game of "Game of Lives".

Author: Quinn Bardwell
Date: 01-30-22
"""

import pygame as pg
import sys
from data.main import main

pg.init()

if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()