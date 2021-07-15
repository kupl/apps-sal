import bisect
from operator import itemgetter
from itertools import groupby

def survivor(zombies):
    if(1 in zombies):
        return 0
    gcdl = False
    for i in zombies:
        if(gcdl==True):
            break
        for x in zombies:
            if(i!=x and gcd(i,x)==1):
                gcdl = True
                break
    if(gcdl == False):
        return -1
    if(len(zombies)==2):
        return zombies[0]*zombies[1]-zombies[0]-zombies[1]
    
    zombies.sort()
    c = zombies.copy()
    e = [1]
    l = max(c)
    N = len(c)
    y=0
    F = zombies[0]*zombies[1]+zombies[0]
    
    for i in range(1,F):
        #print(e)
        x = 0
        for j in range(0,N):
            if(i>=c[j]):
                x+=e[i-c[j]]
        e.append(x)
        e[i] = x
        if(x==0):
            y=i
        
    return y

def gcd(a,b):
    # if a and b are both zero, print an error and return 0
    if a == 0 and b == 0:
        #print("WARNING: gcd called with both arguments equal to zero.",
        #file=sys.stderr)
        return 0
    # make sure a and b are both nonnegative
    if a < 0: a = -a
    if b < 0: b = -b
    while b != 0:
        new_a = b
        new_b = a % b
        a = new_a
        b = new_b
    return a
