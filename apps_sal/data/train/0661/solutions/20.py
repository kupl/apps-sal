try:
    from math import sqrt
    (t, n) = list(map(int, input().split()))
    for _ in range(t):
        x = int(input())
        diff = abs(n / 100 * x)
        ans = int(sqrt(x))
        ans1 = ans ** 2
        if abs(x - ans1) <= diff:
            print('yes')
        else:
            print('no')
except:
    pass
