class Game():
    
    def __init__(self, s):
        self.s = s
        self.sq = [ { d+(2*s+1)*y+x for d in [0, s, s+1, 2*s+1] } for x in range(1,s+1) for y in range(s) ]
        
    def play(self, lines):
        lines, prevlen = set(lines), 0
        while len(lines) != prevlen:
            keep, prevlen = [], len(lines)
            for sq in self.sq:
                if len(sq & lines) >= 3: lines |= sq
                else: keep.append(sq)
            self.sq = keep
        return [n for n in range(1,(2*self.s+2)*self.s+1) if n in lines]
