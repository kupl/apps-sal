from itertools import chain

class Sudoku(object):

    def __init__(self, grid):
        self.grid = grid
        self.size = len(grid)
        self.good_zone = set(range(1, self.size + 1))
    
    def __iter__(self):
        """Iterate over each row, column and square of the sudoku"""
        rows = self.grid
        cols = zip(*rows)
        square_size = int(self.size ** 0.5)
        squares = [sum((rows[y+i][x:x+square_size]
                        for i in range(square_size)), [])
                   for y in range(0, self.size, square_size)
                   for x in range(0, self.size, square_size)]
        return chain(rows, cols, squares)
    
    def valid_data_types(self):
        """Check data types"""
        return all(type(num) == int for num in chain(*self.grid))
    
    def zone_is_valid(self, zone):
        """Check if a zone contain every numbers"""
        return set(zone) == self.good_zone
    
    def is_valid(self):
        """Is the sudoku solved"""
        if not self.valid_data_types(): return False
        return all(self.zone_is_valid(zone) for zone in self)
