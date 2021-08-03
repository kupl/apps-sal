from math import floor as f
for _ in range(int(input())):
    x, N = list(map(int, input().split()))
    xx = x
    su = 0
    t = 1
    c = 1
    while x < N:
        su += x
        c += 1
        x = xx * c
    print(su)
