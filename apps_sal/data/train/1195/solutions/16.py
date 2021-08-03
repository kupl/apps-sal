# cook your dish here
for _ in range(int(input())):
    n, a, b, c, d, p, q, y = map(int, input().split())
    x = list(map(int, input().split()))
    w = abs(x[b - 1] - x[a - 1]) * p
    t = abs(x[d - 1] - x[c - 1]) * q + abs(x[d - 1] - x[b - 1]) * p
    if abs(x[c - 1] - x[a - 1]) * p > y:
        print(w)
    else:
        t = t + y
        print(min(t, w))
