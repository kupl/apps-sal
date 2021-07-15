from itertools import groupby

def interpreter(tape):
    itertic = Tick()
    return itertic(tape)
    
class Tick:
    
    instr = {'+':'_incrm', '*':'_addAs', '<':'_movL','>':'_movR'}

    def __init__(self):
        self.val  = None
        self.doc  = ''
        self.word = ''
        self.s    = 0
        
    def __call__(self,instruct):
        for ins, cnt in [(self.instr[k], int(len(list(v)))) for k,v in groupby(instruct)]:
            getattr(self, ins)(cnt) 
        return self.word
        
    def _movR(self, step):
        self.s += step
        self.val = None
    
    def _movL(self, step):
        self.s -= step
        self.val = self.doc[self.s%len(self.doc)]
    
    def _incrm(self, val):
        self.val = chr( val%255 )
        if self.val not in self.doc: self.doc += self.val
        
    def _addAs(self, r):
        self.word += self.val * r

