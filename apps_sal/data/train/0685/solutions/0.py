# https://www.codechef.com/problems/RECTLIT

def assess(sq,points):
    EWct = 0
    NSct = 0
    for a,b in points:
        EW = (a == 0 or a == sq)
        NS = (b == 0 or b == sq)
        if EW and NS:
            return 'yes'
        EWct += EW
        NSct += NS
    if NSct + EWct == 0 or len(points) == 1:
        return 'no'
    if EWct >= 2 or NSct >= 2:
        return 'yes'
    if len(points) == 2:
        return 'no'
    # now 3 points
    if NSct == 1 and EWct == 1:
        return 'yes'
    # 3 points, one on edge
    x = -1
    for a,b in points:
        if EWct > 0:
            if a == 0 or a == sq:
                e = b
            elif x == -1:
                x = b
            else:
                y = b
        else:
            if b == 0 or b == sq:
                e = a
            elif x == -1:
                x = a
            else:
                y = a
    if (e-x)*(e-y) < 0: # edge splits mids
        return 'no'
    else:
        return 'yes'


for ti in range(int(input())):
    k,n = map(int, input().split())
    if k > 3:
        for ki in range(k):
            input()
        print('yes')
    else:
        pos = [tuple(map(int, input().split())) for ki in range(k)]
        print(assess(n-1,pos))


