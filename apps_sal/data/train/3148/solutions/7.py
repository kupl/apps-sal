def simplify(s):
    been = [(0,0)]
    i,j = 0,0
    d = {'<': (-1,0),'>':(1,0),'^':(0,1),'v':(0,-1)}
    t = s
    for p in s:
        x,y = d.get(p)
        i,j = i+x,j+y
        if (i,j) in been:
            idx = been.index((i,j))
            t = t[:idx] + t[len(been):]
            been = been[:idx]
        been.append((i,j))
    return t
