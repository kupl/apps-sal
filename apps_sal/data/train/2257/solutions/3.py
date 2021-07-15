import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None]*T
geta = 20
for qu in range(T):
    N = int(readline())
    A = list(map(lambda x: ord(x)-97, readline().strip()))
    B = list(map(lambda x: ord(x)-97, readline().strip()))
    if any(a > b for a, b in zip(A, B)):
        Ans[qu] = -1
        continue
    res = 0
    table = [[0]*geta for _ in range(geta)]
    for a, b in zip(A, B):
        if a != b:
            table[a][b] = 1
    
    for al in range(geta):
        if sum(table[al]):
            res += 1
            bl = table[al].index(1)
            for cl in range(bl+1, geta):
                table[bl][cl] = table[bl][cl] | table[al][cl]
    Ans[qu] = res
print('\n'.join(map(str, Ans)))
