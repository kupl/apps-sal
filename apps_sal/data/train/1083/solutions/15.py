def mini(a, b):
    if a >= b:
        return b
    else:
        return a


t = eval(input())
while t:
    (n, m, z, l, r, b) = list(map(int, input().split()))
    x = n * m
    y = n * (m + 1)
    if b <= n or m == 1:
        print(mini(x, z + l + r + b))
        t -= 1
        continue
    if z + l + r + n >= x:
        print(x)
        t -= 1
        continue
    A = min(z, x)
    x -= A
    B = min(l, x)
    x -= B
    C = min(r, x)
    x -= C
    p = min(b, x)
    p = min(p, m * ((n + 1) // 2))
    p = min(p, (y - B - C) // 2)
    print(A + B + C + p)
    t -= 1
