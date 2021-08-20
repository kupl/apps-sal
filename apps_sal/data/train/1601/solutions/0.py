for __ in range(int(input())):
    (n, p) = list(map(int, input().split()))
    d = n % (n // 2 + 1)
    if d == 0:
        t = p * p * p
    else:
        t = (p - d) * (p - d) + (p - d) * (p - n) + (p - n) * (p - n)
    print(t)
