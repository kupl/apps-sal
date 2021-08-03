t = int(input())
for _ in range(t):
    n, a, b, c, d, p, q, y = map(int, input().split())
    x = list(map(int, input().split()))
    t1 = p * abs(x[a - 1] - x[b - 1])
    if(abs(x[c - 1] - x[a - 1]) * p <= y):
        t2 = q * abs(x[c - 1] - x[d - 1]) + abs(x[d - 1] - x[b - 1]) * p + y
        print(min(t1, t2))
    else:
        print(t1)
