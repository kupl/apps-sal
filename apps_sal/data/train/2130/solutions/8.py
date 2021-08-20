def g():
    return int(input())


def ncr(n, r):
    if 2 * r > n:
        r = n - r
    a = 1
    for i in range(r):
        a = a * (n - i) // (i + 1)
    return a


k = g()
ans = 1
n2 = g()
for i in range(k - 1):
    n1 = n2
    n2 += g()
    ans = ans * ncr(n2 - 1, n1) % 1000000007
print(ans)
