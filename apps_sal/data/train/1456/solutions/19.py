import math
t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    if a == 1:
        ans = -1
    else:
        ans = 0
    k = ((b - a + 1) * (b + a)) // 2
    ans += k
    if a % 2:
        ans -= math.ceil((b - a + 1) / 2)
    else:
        if b % 2:
            ans -= math.ceil((b - a) / 2)
        else:
            ans -= (b - a) // 2
    i = 2**30
    c = 0
    while i >= 2:
        x = b // i - (a - 1) // i
        d = x - c
        c = x
        ans -= d * i
        if i >= a and i <= b:
            ans -= 1
        i = i // 2
    print(ans)
