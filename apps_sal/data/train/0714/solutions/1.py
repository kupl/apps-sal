import math
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = math.ceil(sum(l) / n)
    ans = 0
    for i in l:
        x = m - i
        if x > 0:
            ans = ans + x
    print(ans)
