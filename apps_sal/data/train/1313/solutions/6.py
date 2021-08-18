import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = l[0]
    for i in range(1, n):
        s = math.gcd(s, l[i])
    if s == 1:
        print(-1)
    elif s % 2 == 0:
        print(2)
    else:
        ans = 0
        for i in range(3, int(s**0.5) + 1):
            if s % i == 0:
                ans = i
                break
        if ans == 0:
            print(s)
        else:
            print(ans)
