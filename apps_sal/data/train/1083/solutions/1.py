t = int(input())
while t:
    t -= 1
    (n, m, z, l, r, b) = list(map(int, input().split()))
    if m != 1:
        if b >= n:
            ba = n
            bl = b - n
        else:
            ba = b
            b1 = 0
        if ba == n:
            if l + r >= n * (m - 1):
                ans = n * m
            else:
                w = (l + r) % (m - 1)
                la = l
                ll = 0
                ra = r
                rl = 0
                x = (m - 1) / 2
                y = n - (l + r) / (m - 1)
                if w == 0:
                    if bl >= x * y:
                        ba += x * y
                        bl = b - ba
                    else:
                        ba = b
                        bl = 0
                else:
                    y -= 1
                    u = m - 1 - w
                    if bl >= u / 2 + x * y:
                        ba += u / 2 + x * y
                        bl = b - ba
                    else:
                        ba = b
                        bl = 0
                za = min(n * m - la - ra - ba, z)
                zl = z - za
                ans = min(n * m, la + ra + ba + za)
        elif l + r >= n * m - b:
            ans = n * m
        else:
            la = l
            ll = 0
            ra = r
            rl = 0
            za = min(n * m - la - ra - ba, z)
            zl = z - za
            ans = min(n * m, la + ra + ba + za)
    else:
        ans = min(n * m, l + r + z + b)
    print(ans)
