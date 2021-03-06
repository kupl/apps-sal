def mod(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 1:
            x = x * y % c
        y = y * y % c
        b /= 2
    return x % c


t = int(input())
num = 10 ** 9 + 7
for i in range(t):
    (n, m, q, k) = list(map(int, input().split()))
    if m <= q:
        print(0)
    else:
        a1 = m - q
        a2 = mod(q + 1, n, num)
        a3 = mod(q - 1, n, num)
        a4 = mod(q, n, num)
        a5 = a2 - 2 * a4 + a3
        ans = a1 * a5
        print(ans % num)
