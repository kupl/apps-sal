for _ in range(int(input())):
    (x, y) = [int(x) for x in input().split()]
    if x < y:
        print(0)
    else:
        s = 0
        for _ in range(y, x, y):
            s += _ % 10
        print(s)
