for t in range(int(input())):
    n = int(input())
    sqrs = 0
    sizeSqr = 0
    while True:
        if n < 1:
            break
        i = 1
        while True:
            if i * i > n:
                sqrs += 1
                sizeSqr = i - 1
                break
            elif i * i == n:
                sqrs += 1
                sizeSqr = i
                break
            i += 1
        n = n - sizeSqr**2
    print(sqrs)
