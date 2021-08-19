for _ in range(eval(input())):
    (r, c, x, y, z) = list(map(int, input().split()))
    s = r * c
    f = x + y + z
    if x + y + z == s:
        m = x
        if m % r == 0 or m % c == 0:
            if m % r == 0:
                p = m // r
                q = c - p
                if p < c:
                    g = z
                    h = y
                    k = r
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
                    (q, k) = (k, q)
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
            if m % c == 0:
                p = m // c
                q = r - p
                if p < r:
                    g = z
                    h = y
                    k = c
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
                    (q, k) = (k, q)
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
        m = y
        if m % r == 0 or m % c == 0:
            if m % r == 0:
                p = m // r
                q = c - p
                if p < c:
                    g = x
                    h = z
                    k = r
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
                    (q, k) = (k, q)
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
            if m % c == 0:
                p = m // c
                q = r - p
                if p < r:
                    g = x
                    h = z
                    k = c
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
                    (q, k) = (k, q)
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
        m = z
        if m % r == 0 or m % c == 0:
            if m % r == 0:
                p = m // r
                q = c - p
                if p < c:
                    g = x
                    h = y
                    k = r
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
                    (q, k) = (k, q)
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
            if m % c == 0:
                p = m // c
                q = r - p
                if p < r:
                    g = x
                    h = y
                    k = c
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
                    (q, k) = (k, q)
                    if g % q == 0:
                        if (k - g / q) * q == h:
                            print('Yes')
                            continue
    print('No')
