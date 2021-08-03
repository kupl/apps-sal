import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = a[0]
    s = 0
    for i in range(n):
        s += a[i]
        if s % (i + 1) == 0:
            ans = max(ans, s // (i + 1))
        else:
            ans = max(ans, (s // (i + 1)) + 1)
    print(ans)
    # case 1
