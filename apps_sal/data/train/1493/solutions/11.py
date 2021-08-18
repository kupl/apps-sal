"""
arrange string in a form that no two 'B' or two 'G' come together, if can't     return -1
cost = |i-j|**t
minimize cost
"""


def solve(s, c):
    bcount = s.count('B')
    gcount = s.count('G')
    if(abs(bcount - gcount) > 1):
        return -1
    B = []
    G = []
    start = 'B'
    cost = 0
    if(bcount < gcount):
        start = 'G'
    iterate = 1
    temp = start
    if(bcount == gcount):
        iterate = 2
    for y in range(iterate):
        for i in range(len(s)):
            if(s[i] != start):
                if(s[i] == 'B'):
                    if(len(G) > 0):
                        t = G.pop(0)
                        cost += abs(t - i)**c
                    else:
                        B.append(i)
                else:
                    if(len(B) > 0):
                        t = B.pop(0)
                        cost += abs(t - i)**c
                    else:
                        G.append(i)
            if(start == 'B'):
                start = 'G'
            else:
                start = 'B'
        if(temp == 'B'):
            start = 'G'
        else:
            start = 'B'
        if(y == 1):
            break
        eqcost = cost
        cost = 0
        B = []
        G = []
    if(bcount == gcount):
        return min(eqcost, cost)
    return eqcost


for t in range(int(input())):
    c = int(input())
    s = input()
    print(solve(s, c))
