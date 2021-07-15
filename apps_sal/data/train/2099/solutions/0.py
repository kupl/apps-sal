3

import sys

def __starting_point():
    
    n, k = list(map(int, sys.stdin.readline().split()))
    l = []
    i = 1
    j = k + 1
    while i <= j:
        l.append(str(i))
        i += 1
        if j > i:
            l.append(str(j))
            j -= 1
    for i in range(k+2, n+1):
        l.append(str(i))
    
    print(' '.join(l))


__starting_point()
