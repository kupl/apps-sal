def mini(a, b):
    if a >= b:
        return b
    else:
        return a


t = eval(input())
while t:
    m, n, z, l, r, b = list(map(int, input().split()))
    x = n * m
    y = m * (n + 1)
    A = min(z, x)
    ans = A
    x -= A
    B = min(l, x)
    ans += B
    x -= B
    C = min(r, x)
    ans += C
    x -= C
    p = min(b, x)
    x = m * ((n + 1) // 2)
    p = min(p, x)
    x = (y - B - C) // 2
    ans += min(p, x)
    print(ans)
    t -= 1
