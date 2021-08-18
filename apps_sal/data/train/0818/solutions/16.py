from bisect import *
t = int(input())
while(t):
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    ref = []
    l = 1
    r = 0
    for i in range(n + 1):
        if(a[i] % 2):
            r += 1
        else:
            if(l and r):
                ref.append([l, r + l - 1])
                l = i + 2
                r = 0
            l = i + 2
    ref1 = []
    for i in ref:
        ref1.append([i[1], i[0]])
    q = int(input())
    while(q):
        q -= 1
        l, r = list(map(int, input().split()))
        it = bisect_left(ref1, [l])
        if(l >= ref1[it][1] and r <= ref1[it][0]):
            print("ODD")
        else:
            print("EVEN")
