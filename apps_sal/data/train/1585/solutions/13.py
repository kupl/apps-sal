for t in range(int(input())):
    (x, y) = map(int, input().split())
    if y > x:
        (x, y) = (y, x)
    print(x, x + y)
