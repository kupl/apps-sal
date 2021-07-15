class Funnel(object):
    
    SIZE = 5
    
    def __init__(self):
        self.fun = [ [None] * (x+1) for x in range(self.SIZE) ]
        
    
    def fill(self, *args):
        genBlanks = ((x,y) for x,r in enumerate(self.fun) for y,v in enumerate(r) if v is None)
        
        for v,(x,y) in zip(args, genBlanks): 
            self.fun[x][y] = v
    
    
    def drip(self):
        y,cnt = 0, sum(v is not None for row in self.fun for v in row)
        drop  = self.fun[0][0]
        
        for x in range(self.SIZE-1):
            left  = cnt - sum( self.fun[xx][y+xx-x] is not None for xx in range(x,self.SIZE))
            right = cnt - sum( self.fun[xx][y] is not None      for xx in range(x,self.SIZE))
            
            ySwp, cnt      = (y,left) if left >= right else (y+1,right)
            self.fun[x][y] = self.fun[x+1][ySwp]
            y = ySwp
            if not cnt: break
        
        self.fun[x+1][y] = None
        return drop
        
    
    def __str__(self):
        return '\n'.join( f'{" "*x}\\{" ".join( " " if v is None else str(v) for v in r)}/'
                          for x,r in enumerate(reversed(self.fun)) )

