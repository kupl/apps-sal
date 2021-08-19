for j in range(int(input())):
    (n, k) = list(map(int, input().split()))
    s = n * (n + 1) / 2
    i = k
    while i <= n:
        s -= i
        i *= k
    print('Case #%d: %d' % (j + 1, s))
