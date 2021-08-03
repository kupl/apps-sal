t = eval(input())
while t > 0:
    t = t - 1
    n, b, m = list(map(int, input().split()))
    s = n / 2
    p = 0
    if n % 2 == 0:
        p = n / 2
    else:
        p = (n + 1) / 2
    ans = 0
    i = 0
    n = n - p
    while n > 0:
        ans = ans + p * m + b
        m = m * 2

        if n % 2 == 0:
            p = n / 2
        else:
            p = (n + 1) / 2
        n = n - p
        i = i + 1
    ans = ans + m
    print(ans)
