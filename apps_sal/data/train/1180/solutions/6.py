for _ in range(int(input())):
    (n, k, x, y) = list(map(int, input().split()))
    if x == y:
        print(n, n)
    else:
        k = (k - 1) % 4 + 1
        if y > x:
            (x, y) = (y, x)
            if k == 1:
                print(y + n - x, n)
            elif k == 2:
                print(n, y + n - x)
            elif k == 3:
                print(x - y, 0)
            else:
                print(0, x - y)
        elif k == 1:
            print(n, y + n - x)
        elif k == 2:
            print(y + n - x, n)
        elif k == 3:
            print(0, x - y)
        else:
            print(x - y, 0)
