from itertools import cycle

MOVES = ((1,1),(0,-1),(-1,0))

def make_triangle(m,n):
    X = ((1+8*(n-m+1))**.5-1) / 2
    if X%1: return ''
    
    X   = int(X)
    tri = [[-1]*(i+1) for i in range(int(X))]
    x,y,v,moves = 0, 0, m%10, cycle(MOVES)
    dx,dy = next(moves)
    for _ in range(n-m+1):
        tri[x][y] = str(v)
        v = (v+1)%10
        if not (0<=x+dx<X and 0<=y+dy<X) or tri[x+dx][y+dy]!=-1:
            dx,dy = next(moves)
        x+=dx ; y+=dy
    return '\n'.join(' '*(X-i-1)+' '.join(row) for i,row in enumerate(tri))
