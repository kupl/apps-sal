from itertools import product

def sat(f: Formula):

    def getLiterals(f,s):
        if f.is_literal(): s.add(f)
        else:
            for n in f.args: getLiterals(n,s)
        return s
        
    def evaluate(f,bools):
        return ( bools[f] if f.is_literal() else 
                 any(evaluate(n,bools) for n in f.args) if f.is_or() else
                 all(evaluate(n,bools) for n in f.args) ^ f.is_not() )
                 
    lst = list(getLiterals(f,set()))
    for p in product([0,1],repeat=len(lst)):
        bools = dict(zip(lst,p))
        if evaluate(f,bools):
            return {n for n,v in bools.items() if v}
    return False
