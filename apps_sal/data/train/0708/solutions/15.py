for _ in range(int(input())):
    (n, s) = list(map(int, input().split()))
    (p, count) = (1, 0)
    for i in range(1, n + 1):
        c = pow(s, 2 * i - 1, 10 ** 9 + 7)
        s *= c
        s = s % (10 ** 9 + 7)
        count = (count + c) % (10 ** 9 + 7)
    print(count)
