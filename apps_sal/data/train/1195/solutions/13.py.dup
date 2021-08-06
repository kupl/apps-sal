t = int(input())
for _ in range(t):
    n, a, b, c, d, p, q, y = list(map(int, input().split()))
    x = list(map(int, input().split()))

    time1 = p * abs(x[a - 1] - x[b - 1])
    l = p * abs(x[a - 1] - x[c - 1])
    if l <= y:
        time2 = (q * abs(x[c - 1] - x[d - 1])) + (p * abs(x[d - 1] - x[b - 1])) + y
        print(min(time1, time2))
    else:
        print(time1)
