t = int(input())


def power(x, y):
    res = 1
    x = x % mod
    while y > 0:
        if y & 1 == 1:
            res = res * x % mod
        y = y >> 1
        x = x * x % mod
    return res


for tc in range(t):
    (n, m1) = input().split()
    (n, m1) = (int(n), int(m1))
    print('Case ' + str(tc + 1) + ':')
    for i in range(m1):
        s = input()
        k = len(s)
        mod = 10 ** 9 + 7
        m = n - k
        if k > n:
            print(0)
        else:
            print((m + 1) * power(26, m) % mod)
