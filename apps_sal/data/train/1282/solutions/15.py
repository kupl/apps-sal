mod = 10 ** 9 + 7
for _ in range(int(input())):
    (l, r) = map(int, input().split())
    z = 2
    while z <= l:
        z *= 2
    if r > z:
        r = z - 1
    z = z // 2
    ans = l
    lb = bin(l).replace('0b', '')
    for i in lb:
        if i != '0':
            h = l % z
            h = z - h - 1
            if h >= r - l:
                g = r % z
                g = z - g - 1
                if g < h:
                    h = h - g
            ans += h * z
        z = z // 2
    print(ans % mod)
