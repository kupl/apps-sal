import itertools
class Nonogram:
    poss = {(1,1,1): set([(1,0,1,0,1)]),
            (1,1):   set([(0,0,1,0,1),(0,1,0,1,0),(1,0,1,0,0),(0,1,0,0,1),(1,0,0,1,0),(1,0,0,0,1)]),
            (1,2):   set([(1,0,1,1,0),(1,0,0,1,1),(0,1,0,1,1)]),
            (1,3):   set([(1,0,1,1,1)]),
            (2,1):   set([(1,1,0,1,0),(1,1,0,0,1),(0,1,1,0,1)]),
            (2,2):   set([(1,1,0,1,1)]),
            (3,1):   set([(1,1,1,0,1)]),
            (1,):    set([(0,0,0,0,1),(0,0,0,1,0),(0,0,1,0,0),(0,1,0,0,0),(1,0,0,0,0)]),
            (2,):    set([(0,0,0,1,1),(0,0,1,1,0),(0,1,1,0,0),(1,1,0,0,0)]),
            (3,):    set([(0,0,1,1,1),(0,1,1,1,0),(1,1,1,0,0)]),
            (4,):    set([(0,1,1,1,1),(1,1,1,1,0)]),
            (5,):    set([(1,1,1,1,1)])}
    
    def __init__(self, clues):
        self.h,self.w=(tuple(Nonogram.poss[clue] for clue in side) for side in clues)

    def solve(self):
        for r in itertools.product(*self.w):
            if all(c in self.h[i] for i,c in enumerate(zip(*r))): return r

