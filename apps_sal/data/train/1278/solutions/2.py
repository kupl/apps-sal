t = int(input())
e = 10 ** 9 + 7
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    c = min(a, b)
    x = c * (c + 1) // 2
    c -= 1
    xx = c * (c + 1) // 2
    (y, z) = (c * (c + 1) * (2 * c + 1) // 6, xx * xx)
    ans = x * a * b + y + z
    ans -= (xx + y) * (a + b)
    print(ans % e)
