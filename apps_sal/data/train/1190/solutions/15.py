t = int(input())
i = 0
while i < t:
    n = int(input())
    c = 0
    if n > 2048:
        c = n // 2048
        n = n - c * 2048
    while n > 0:
        r = n % 2
        if r == 1:
            c += 1
        n = n // 2
    print(c)
    i += 1
