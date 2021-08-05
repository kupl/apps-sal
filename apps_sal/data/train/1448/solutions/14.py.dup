t = int(input())
for _ in range(t):
    a, d, k, n, inc = map(int, input().split())
    a -= d
    day = 0
    while day < n:
        for j in range(k):
            a += d
            day += 1
            if day == n:
                break
        d += inc
    print(a)
