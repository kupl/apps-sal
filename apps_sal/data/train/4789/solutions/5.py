from itertools import product

def evaluate(self):
    return ( self.val if self.is_literal() else
             all(n.evaluate() for n in self.args) if self.is_and() else
             any(n.evaluate() for n in self.args) if self.is_or() else
             not self.args[0].evaluate() )

Formula.evaluate=evaluate


def sat(f: Formula):
    
    def travel(f):
        if f.is_literal(): s.add(f)
        else:              
            for n in f.args:
                travel(n)
    
    s=set()
    travel(f)
    lst = list(s)
    for p in product([0,1], repeat=len(lst)):
        s=set()
        for n,v in zip(lst,p):
            n.val=v
            if v: s.add(n)
        if f.evaluate(): return s
    return False
