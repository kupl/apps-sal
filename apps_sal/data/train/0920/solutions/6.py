def ans(x, g):
    return x * g * g + ((x * (x - 1)) // 2) * g


for _ in range(int(input())):
    s = list(input())
    g, b = s.count('g'), s.count('b')
    if g > b:
        g, b = b, g
    n = (g - 1)
    co = 0
    co += ((n) * (n + 1) * (2 * n + 1)) // 3
    b = b - (g - 1)
    if b % 2 == 0:
        x = b // 2
        co += 2 * ans(x, g)
    else:
        x, y = b // 2, b // 2 + 1
        co += ans(x, g) + ans(y, g)
    if co <= 0:
        print(0)
    else:
        print(co)
