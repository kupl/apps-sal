(n, h) = map(int, input().split())
unit = h * h / n
for i in range(1, n):
    print((unit * i) ** 0.5, end=' ')
