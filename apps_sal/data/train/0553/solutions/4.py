for _ in range(int(input())):
    (a, b, c) = map(int, input().split())
    (p, q, r) = map(int, input().split())
    zeros = [a, b, c].count(0)
    (d, e, f) = (p - a, q - b, r - c)
    operations = 0
    if d == e == f:
        if d:
            operations = 1
        else:
            operations = 0
    elif zeros >= 2:
        if d == e and f == 0 or (d == e == 0 and f) or (e == f and d == 0) or (e == f == 0 and d) or (f == d and e == 0) or (f == d == 0 and e):
            operations = 1
        elif d == e or e == f or f == d or (d == e + f) or (e == d + f) or (f == d + e):
            operations = 2
    elif zeros == 1:
        if a == 0:
            if d == e and f == 0 or (d == e == 0 and f) or (e == f and d == 0) or (e == f == 0 and d) or (f == d and e == 0) or (f == d == 0 and e) or (d == 0 and q // b == r // c and (q % b == 0) and (r % c == 0)):
                operations = 1
            elif d == e or e == f or f == d or (d and q // b == r // c and (q % b == 0) and (r % c == 0)) or (d == e + f) or (e == d + f) or (f == d + e):
                operations = 2
        elif b == 0:
            if d == e and f == 0 or (d == e == 0 and f) or (e == f and d == 0) or (e == f == 0 and d) or (f == d and e == 0) or (f == d == 0 and e) or (e == 0 and p // a == r // c and (p % a == 0) and (r % c == 0)):
                operations = 1
            elif d == e or e == f or f == d or (e and p // a == r // c and (p % a == 0) and (r % c == 0)) or (d == e + f) or (e == d + f) or (f == d + e):
                operations = 2
        elif d == e and f == 0 or (d == e == 0 and f) or (e == f and d == 0) or (e == f == 0 and d) or (f == d and e == 0) or (f == d == 0 and e) or (f == 0 and p // a == q // b and (p % a == 0) and (q % b == 0)):
            operations = 1
        elif d == e or e == f or f == d or (f and p // a == q // b and (p % a == 0) and (q % b == 0)) or (d == e + f) or (e == d + f) or (f == d + e):
            operations = 2
    else:
        (x, y, z) = (p // a, q // b, r // c)
        if d == e and f == 0 or (d == e == 0 and f) or (e == f and d == 0) or (e == f == 0 and d) or (f == d and e == 0) or (f == d == 0 and e) or (x == y == z and p % a == 0 and (q % b == 0) and (r % c == 0)) or (d == 0 and y == z and (q % b == 0) and (r % c == 0)) or (e == 0 and x == z and (p % a == 0) and (r % c == 0)) or (f == 0 and x == y and (p % a == 0) and (q % b == 0)):
            operations = 1
        elif d == e or e == f or f == d or (f and x == y and (p % a == 0) and (q % b == 0)) or (d and y == z and (q % b == 0) and (r % c == 0)) or (e and x == z and (p % a == 0) and (r % c == 0)) or (d == 0 and e != f and e and f) or (e == 0 and d != f and d and f) or (f == 0 and d != e and d and e) or (d == e + f) or (e == d + f) or (f == d + e) or (p % a == 0 and q % b == 0 and (r % c == 0) and (x * y == z or y * z == x or z * x == y)):
            operations = 2
    if operations == 0:
        if d:
            operations += 1
        if e:
            operations += 1
        if f:
            operations += 1
    if operations == 3:
        try:
            (u, v, w) = ((q * a - p * b) // (p - q), (r * b - q * c) // (q - r), (p * c - r * a) // (r - p))
            if u == v == w and (q * a - p * b) % (p - q) == 0 and ((r * b - q * c) % (q - r) == 0) and ((p * c - r * a) % (r - p) == 0) and (p // (a + u) == q // (b + u) == r // (c + u)) and (p % (a + u) == 0) and (q % (b + u) == 0) and (r % (c + u) == 0):
                operations = 2
        except:
            pass
        if operations == 3:
            try:
                x = p // a
                if p % a == 0 and (q % x == 0 and c + q // x - b == r or (r % x == 0 and b + r // x - c == q)):
                    operations = 2
            except:
                pass
            if operations == 3:
                try:
                    x = q // b
                    if q % b == 0 and (p % x == 0 and c + p // x - a == r or (r % x == 0 and a + r // x - c == p)):
                        operations = 2
                except:
                    pass
                if operations == 3:
                    try:
                        x = r // c
                        if r % c == 0 and (p % x == 0 and b + p // x - a == q or (q % x == 0 and a + q // x - b == p)):
                            operations = 2
                    except:
                        pass
                    if operations == 3:
                        try:
                            if (q * a - p * b) % (p - q) == 0:
                                (u, x) = ((q * a - p * b) // (p - q), p // (a + u))
                                if x == q // (b + u) and p % (a + u) == 0 and (q % (b + u) == 0) and (c * x == r or c + u == r):
                                    operations = 2
                        except:
                            pass
                        if operations == 3:
                            try:
                                if (r * b - q * c) % (q - r) == 0:
                                    (v, x) = ((r * b - q * c) // (q - r), q // (b + v))
                                    if x == r // (c + v) and q % (b + v) == 0 and (r % (c + v) == 0) and (a * x == p or a + v == p):
                                        operations = 2
                            except:
                                pass
                            if operations == 3:
                                try:
                                    if (p * c - r * a) % (r - p) == 0:
                                        (w, x) = ((p * c - r * a) // (r - p), r // (c + w))
                                        if x == p // (a + w) and r % (c + w) == 0 and (p % (a + w) == 0) and (b * x == q or b + w == q):
                                            operations = 2
                                except:
                                    pass
                                if operations == 3:
                                    try:
                                        (x, y, z) = ((p - q) // (a - b), (q - r) // (b - c), (r - p) // (c - a))
                                        if x == y == z and (p - q) % (a - b) == 0 and ((q - r) % (b - c) == 0) and ((r - p) % (c - a) == 0) and (p - a * x == q - b * y == r - c * z):
                                            operations = 2
                                    except:
                                        pass
                                    if operations == 3:
                                        try:
                                            x = p // a
                                            if p % a == 0 and (b * x + r - c == q or c * x + q - b == r):
                                                operations = 2
                                        except:
                                            pass
                                        if operations == 3:
                                            try:
                                                x = q // b
                                                if q % b == 0 and (a * x + r - c == p or c * x + p - a == r):
                                                    operations = 2
                                            except:
                                                pass
                                            if operations == 3:
                                                try:
                                                    x = r // c
                                                    if r % c == 0 and (a * x + q - b == p or b * x + p - a == q):
                                                        operations = 2
                                                except:
                                                    pass
                                                if operations == 3:
                                                    try:
                                                        x = (p - q) // (a - b)
                                                        if (p - q) % (a - b) == 0 and p - a * x == q - b * x and (c + p - a * x == r or c * x == r):
                                                            operations = 2
                                                    except:
                                                        pass
                                                    if operations == 3:
                                                        try:
                                                            y = (q - r) // (b - c)
                                                            if (q - r) % (b - c) == 0 and q - b * y == r - c * y and (a + q - b * y == p or a * y == p):
                                                                operations = 2
                                                        except:
                                                            pass
                                                        if operations == 3:
                                                            try:
                                                                z = (r - p) // (c - a)
                                                                if (r - p) % (c - a) == 0 and r - c * z == p - a * z and (b + r - c * z == q or b * z == q):
                                                                    operations = 2
                                                            except:
                                                                pass
    print(operations)
