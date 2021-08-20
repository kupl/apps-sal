for _ in range(int(input())):
    (x, n) = list(map(int, input().split()))
    nn = n // x
    ss = nn * (x + x * nn) // 2
    if n % x == 0:
        print(ss - n)
    else:
        print(ss)
