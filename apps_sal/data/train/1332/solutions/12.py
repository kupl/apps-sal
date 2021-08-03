n = int(input())
for j in range(n):
    a, b = list(map(int, input().split()))
    d = 0
    while a != b:
        if a > b:
            a /= 2
            d += 1
        else:
            b /= 2
            d += 1
    print(d)
