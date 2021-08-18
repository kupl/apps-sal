for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x = (a - b + c) // 2
    y = (a - c + b) // 2
    z = (b + c - a) // 2
    print(x, y, z)
