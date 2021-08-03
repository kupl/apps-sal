t = int(input())
for _ in range(t):
    x, r, a, b = list(map(int, input().split()))
    wa = a / r
    wb = b / r
    wd = abs(wa - wb)
    time = x / max(wa, wb)
    dist = wd * time
    if(dist == int(dist)):
        ans = int(dist) - 1
    else:
        ans = int(dist)
    print(ans)
