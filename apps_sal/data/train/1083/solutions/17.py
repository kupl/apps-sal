def func(n, m, z, l, r, b):
    l = l + r
    if l >= n * (m - 1):
        return min(n * m, l + z + b)
    x = l / (m - 1)
    ans = x * (m - 1)
    x = min(b, x)
    ans = ans + x
    b = b - x
    x = l % (m - 1)
    ans = ans + x
    x = m - x
    x = min(x / 2 + x % 2, b)
    ans = ans + x
    b = b - x
    x = n - l / (m - 1)
    x = x - 1
    x = min(b, x * (m / 2 + m % 2))
    ans = ans + x
    z = min(z, n * m - ans)
    ans = ans + z
    return ans


def func2(n, m, z, l, r, b):
    l = l + r
    if l >= n * (m - 1):
        return min(n * m, l + z + b)
    x = l / (m - 1)
    ans = x * (m - 1)
    n2 = n - x
    x = min(b, x)
    ans = ans + x
    b = b - x
    l = l % (m - 1)
    x = l / n2
    ans = ans + x * n2
    m = m - x
    l = l % n2
    ans1 = ans + func(n2, m, z, l, 0, b)
    ans2 = 0
    ans3 = 0
    if l > 0:
        ans2 = ans + l
        x = min(z, n2 - l)
        ans2 = ans2 + x
        z = z - x
        m = m - 1
        ans2 = ans2 + func(n2, m, z, 0, 0, b)
        z = z + x
        m = m + 1
        ans3 = ans + l
        x = min(b, n2 - l)
        ans3 = ans3 + x
        b = b - x
        m = m - 2
        ans3 = ans3 + func(n2, m, z, 0, 0, b)
    return max(ans, ans2, ans3)


t = eval(input())
for _ in range(0, t):
    (n, m, z, l, r, b) = list(map(int, input().split()))
    a = func(n, m, z, l, r, b)
    a = max(a, func2(n, m, z, l, r, b))
    print(a)
