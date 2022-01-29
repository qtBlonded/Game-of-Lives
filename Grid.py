"""
This is a class implementation for the Grid our game of life.

Author: Quinn Bardwell
Date: 01-29-22
"""

class Grid:


    def __init__(self, rows=10, cols=10):
        self.rows_size = rows
        self.cols_size = cols

        self.grid = []
        for _ in range(self.rows_size):
            self.grid.append([0] * self.cols_size)
    
    def next_step(self):
        pass
    
    def insert(self, cell_data):
        color, row, col = cell_data
        assert 0 <= row < self.rows_size
        assert 0 <= col < self.cols_size

        self.grid[row][col] = color
    
    def grid_print(self):
        print("-" * (self.cols_size*2 - 1))
        for row in self.grid:
            print(" ".join([str(val) for val in row]))
        print("-" * (self.cols_size*2 - 1) + "\n")

    def _valid_adj(row, col):
        pass

    def _alive_adj(row, col):
        pass
    
    def _is_alive_next_step(row, col):
        pass


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