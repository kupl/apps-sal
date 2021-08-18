for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    n -= 1
    m -= 1

    if n % x == 0 and m % y == 0:
        print("Chefirnemo")
    else:
        n -= 1
        m -= 1
        if n % x == 0 and m % y == 0:
            if n >= 0 and m >= 0:
                print("Chefirnemo")
            else:
                print("Pofik")
        else:
            print("Pofik")
