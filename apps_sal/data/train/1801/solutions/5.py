def interpreter(code, iterations, width, height):
    inter = Inter(code, width, height)
    inter.run(iterations)
    return '\r\n'.join(''.join(e) for e in inter.grid)
    
class Inter:
    _instruct = { 'w':'moveW', 'e':'moveE', 'n':'moveN', 's':'moveS', '*':'flip', '[':'jumpP', ']':'jumpB'} 
    _nonC = lambda x:None
    def __init__(self, code, w, h):
        self.com = code
        self.grid = [['0']*w for e in range(h)]
        self.x, self.y  = 0, 0
        self.w, self.h  = w, h
        self.i, self.it = 0, 0
        
    def countIteration(f):
        def wrap(cls):
            cls.it += 1
            return f(cls)
        return wrap
    
    def run(self, iterat):
        while self.it < iterat and self.i < len(self.com):#
            getattr(self, self._instruct.get(self.com[self.i],'_nonC'))()
            self.i += 1
        
    @countIteration
    def moveE(self):
        self.x = (self.x + 1)%self.w
    
    @countIteration
    def moveW(self):
        self.x = (self.x - 1)%self.w
        
    @countIteration
    def moveN(self):
        self.y = (self.y - 1)%self.h
        
    @countIteration
    def moveS(self):
        self.y = (self.y + 1)%self.h
    
    @countIteration
    def flip(self):
        self.grid[self.y][self.x] = '10'[int(self.grid[self.y][self.x])]
    
    @countIteration
    def jumpP(self):
        if self.grid[self.y][self.x] == '0':
            self._jump(1,  ']', '[')
    
    @countIteration
    def jumpB(self):
        if self.grid[self.y][self.x] == '1':
            self._jump(-1, '[', ']')
        
    def _jump(self, way, need, past, nest = 0):
        while way:
            self.i += way
            if self.com[self.i] == need and not nest: break
            if self.com[self.i] == need and nest: nest -= 1
            if self.com[self.i] == past: nest += 1

