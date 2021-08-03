try:
    from math import ceil
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(ceil(n / 2) * k)
except EOFError:
    pass
