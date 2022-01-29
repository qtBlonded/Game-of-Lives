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
        temp = []
        for _ in range(self.rows_size):
            temp.append([0] * self.cols_size)
        
        for row in range(self.rows_size):
            for col in range(self.cols_size):
                temp[row][col] = self._cell_next_step(row, col)
        self.grid = temp
    
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

    def _valid_adj(self, row, col):
        valid = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < self.rows_size and 0 <= col + j < self.cols_size and not (i == 0 and j == 0):
                    valid.append((row + i, col + j))
        return valid

    def _alive_adj(self, row, col):
        valid_adj = self._valid_adj(row, col)
        return [(row, col) for row, col in valid_adj if self.grid[row][col] > 0]

    def _cell_next_step(self, row, col):
        alive_adj = self._alive_adj(row, col)
        if self.grid[row][col] == 0:
            return 1 if len(alive_adj) == 3 else 0
        return 1 if len(alive_adj) == 2 or len(alive_adj) == 3 else 0


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