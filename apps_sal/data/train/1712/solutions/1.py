from collections import defaultdict


def puzzle_solver(pieces, h, w):
    pool   = defaultdict(lambda:defaultdict(int))
    pieces = [ Piece(a,b,i,pool) for a,b,i in pieces ]
    return next(p for p in pieces if p.isTopLeft()).build()


class Piece(object):

    def __init__(self,a,b,i,pool):
        self.U,self.D,self.L,self.R = a,b,*zip(a,b)
        self.id,self.pool = i,pool
        for d,r in zip('UDLR','DURL'):
            k = getattr(self,d)
            if k!=(None,None): pool[k][r] = self
    
    def isTopLeft(self): return self.U == self.L == (None,None)
    def build(self):     return [ tuple(pp.id for pp in p._iter('R')) for p in self._iter('D')]
        
    def _iter(piece,d):
        while piece:
            yield piece
            piece = piece.pool[getattr(piece,d)][d]
