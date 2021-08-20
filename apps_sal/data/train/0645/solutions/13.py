for _ in range(int(input())):
    n = int(input())
    k = int(input())
    if k % n == 0:
        print(0)
    elif n % 2 == 0:
        x = n // 2
        if k % x == 0:
            print(n - 1)
        else:
            y = k % n
            if y > x:
                y = n - y
            print(2 * y)
    else:
        x = n // 2
        y = x + 1
        if (k - x) % n == 0 or (k - y) % n == 0:
            print(n - 1)
        else:
            z = k % n
            if z > x:
                z = n - z
            print(2 * z)
