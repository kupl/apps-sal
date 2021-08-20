for i in range(int(input())):
    (x, n) = map(int, input().split())
    s = 0
    if n == x:
        print('0')
    else:
        a = int((n - 1) / x)
        s = a * (2 * x + (a - 1) * x) / 2
        print(int(s))
