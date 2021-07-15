import math
for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    ans = 0
    p, q = map(int, input().split())
    for i in range(n//2):
        a = ar[i]
        b = ar[-(i+1)]
        t1 = math.atan((p-a)/q)
        t2 = math.atan((b-p)/q)
        ans += (t1+t2)
    print(ans)
