from itertools import chain
import math

class Sudoku(object):

    def __init__(self, data):
        self.grip = data
        self.len = len(data)
        self.valid = (self.len == 1 and data != [[1]]) or not all(( len(e) == self.len for e in data )) or all(type(x)!=int for e in data for x in e )
        self.box = int(math.sqrt(self.len))
    
    def resp(self):
        self.grip = list( zip( *[ list( zip( *[iter(e)]*self.box)) for e in self.grip][::-1] ))
        return [list(chain(*list( zip( *[iter(e)]*self.box))[i]))  for e in self.grip for i in range(len(self.grip)//self.box)]
                 
    def is_valid(self): 
        return not self.valid and all(( len(set(e)) == self.len  for e in self.resp() ))
