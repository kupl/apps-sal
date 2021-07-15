def drop(p):
    p[0][0]=''; x=0;
    for y in range(1,len(p)):
        dx = 1 if not p[y][x] else 0 if not p[y][x+1] else 1 if p[y][x+1]<p[y][x] else 0
        p[y-1][x]=p[y][x+dx]; x+=dx
    p[-1][x]=''

def funnel_out(funnel):
    s=[]; p=[r[:] for r in reversed(funnel)]
    while p[0][0]: s.append(p[0][0]); drop(p)
    return ''.join(s)
