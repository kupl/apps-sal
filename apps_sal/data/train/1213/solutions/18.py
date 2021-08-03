for t in range(int(input())):
    x1, x2, x3, v1, v2 = map(int, input().split())
    a = abs(x1 - x3)
    b = abs(x2 - x3)
    g = a / v1
    h = b / v2
    if g > h:
        print("Kefa")
    elif g == h:
        print("Draw")
    else:
        print("Chef")
