NN = 18
BIT=[0]*(2**NN+1)

def addbit(i, x):
    while i <= 2**NN:
        BIT[i] += x
        i += i & (-i)

def getsum(i):
    ret = 0
    while i != 0:
        ret += BIT[i]
        i -= i&(-i)
    return ret

def searchbit(x):
    l, sl = 0, 0
    d = 2**(NN-1)
    while d:
        m = l + d
        sm = sl + BIT[m]
        if sm <= x:
            l, sl = m, sm
        d //= 2
    return l
    
N = int(input())
A = [int(a) for a in input().split()]
for i in range(1, N+1):
    addbit(i, i)

ANS = []
for s in A[::-1]:
    a = searchbit(s) + 1
    addbit(a, -a)
    ANS.append(a)
    
print(*ANS[::-1])
