t = int(input())
while t != 0:
    n = int(input())
    k = int(input())
    if k % n == 0:
        print(0)
    else:
        p = k % n
        if n % 2 == 0 and p == n / 2:
            print(2 * p - 1)
        elif p > n // 2:
            print(2 * (n - p))
        else:
            print(2 * p)
    t -= 1
