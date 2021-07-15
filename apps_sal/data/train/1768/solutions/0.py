from itertools import chain

def fit_bag(H, W, items):

    def deploy(item):
        X,Y    = len(item), len(item[0])
        v      = (set(chain.from_iterable(item))-{0}).pop()
        deltas = [(x,y) for x,r in enumerate(item) for y,n in enumerate(r) if n]
        return (len(deltas), X*Y, max(X,Y), min(X,Y), X,Y,deltas,v)
    
    def dfs(i=0):
        if i==len(items): yield bag
        _,_,_,_,X,Y,deltas,v = items[i]
        for x in range(H-X+1):
            for y in range(W-Y+1):
                if all(not bag[x+dx][y+dy] for dx,dy in deltas):
                    for dx,dy in deltas: bag[x+dx][y+dy] = v
                    yield from dfs(i+1)
                    for dx,dy in deltas: bag[x+dx][y+dy] = 0
    
    bag   = [ [0]*W for _ in range(H) ]
    items = sorted(map(deploy,items), reverse=True)
    return next(dfs())
