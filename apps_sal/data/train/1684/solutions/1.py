from math import tan, sqrt, pi, floor, ceil
for _ in range(int(input())):
    n = int(input())
    y = 0
    for i in range(1, 1001):
        p = n * i ** 3
        if floor(sqrt(p)) == ceil(sqrt(p)):
            y = i
            break
    x = [y] * n
    print(*x)
