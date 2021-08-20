def d1d2(p, q, r, a, b, c):
    if p == 0 or q == 0 or r == 0:
        return False
    if a % p == 0 and b % q == 0:
        d1 = a // p
        d2 = b // q
        if c == r * d1 * d2:
            return True
        return False
    return False


def e1e2(p, q, r, a, b, c):
    e1 = a - p
    e2 = b - q
    return c == r + e1 + e2


def d3e3(p, q, r, a, b, c):
    delta = [0, 0, 0]
    delta[0] = p - q
    if delta[0] == 0:
        return False
    delta[1] = a - b
    delta[2] = p * b - q * a
    if delta[1] % delta[0] == 0 and delta[2] % delta[0] == 0:
        val_d = delta[1] // delta[0]
        val_e = delta[2] // delta[0]
        return c == r * val_d + val_e
    else:
        return False


def d3e2(p, q, r, a, b, c):
    delta = [0, 0, 0]
    delta[0] = p - q
    if delta[0] == 0:
        return False
    delta[1] = a - b
    delta[2] = p * b - q * a
    if delta[1] % delta[0] == 0 and delta[2] % delta[0] == 0:
        val_d = delta[1] // delta[0]
        val_e = delta[2] // delta[0]
        return c == r * val_d
    else:
        return False


def d2e3(p, q, r, a, b, c):
    delta = [0, 0, 0]
    delta[0] = p - q
    if delta[0] == 0:
        return False
    delta[1] = a - b
    delta[2] = p * b - q * a
    if delta[1] % delta[0] == 0 and delta[2] % delta[0] == 0:
        val_d = delta[1] // delta[0]
        val_e = delta[2] // delta[0]
        return c == r + val_e
    else:
        return False


'\ntwo case: 1. a = pd + e, b = qd + e, c = r (already handled 1 same)\n2. a = pd + e, b = qd, c = r + e\n'


def d2e2(p, q, r, a, b, c):
    if q != 0 and b % q == 0:
        d = b // q
        e = c - r
        assert e != 0, 'already checked, one same'
        return a == p * d + e
    return False


def e3d2(p, q, r, a, b, c):
    assert c != r, '1 same'
    e = c - r
    if p != -e and q != -e and (a % (p + e) == 0) and (b % (q + e) == 0):
        d1 = a // (p + e)
        d2 = b // (q + e)
        return d1 != 1 and d1 == d2
    return False


def e2d2(p, q, r, a, b, c):
    if r != 0 and c % r == 0:
        d = c // r
        e = b - q
        assert d != 1 and e != 0, '1 or 2 same'
        return a == (p + e) * d
    return False


def modified(src, dst):
    (p, q, r) = src
    (a, b, c) = dst
    if p == a and q == b and (r == c):
        print(0)
        return
    if p == a and q == b:
        if r != c:
            print(1)
            return
        assert True, 'Should not have come here1'
    if q == b and r == c:
        if p != a:
            print(1)
            return
        assert True, 'Should not have come here2'
    if r == c and p == a:
        if q != b:
            print(1)
            return
        assert True, 'Should not have come here3'
    if p == a:
        if b - q == c - r:
            print(1)
            return
        if q != 0 and r != 0 and (b % q == 0) and (b % q == c % r) and (b // q == c // r):
            print(1)
            return
        print(2)
        return
    if q == b:
        if c - r == a - p:
            print(1)
            return
        if p != 0 and r != 0 and (a % p == 0) and (a % p == c % r) and (a // p == c // r):
            print(1)
            return
        print(2)
        return
    if r == c:
        if b - q == a - p:
            print(1)
            return
        if p != 0 and q != 0 and (a % p == 0) and (a % p == b % q) and (a // p == b // q):
            print(1)
            return
        print(2)
        return
    if p - a == q - b and q - b == r - c:
        print(1)
        return
    if p != 0 and q != 0 and (r != 0):
        if a % p == 0 and a % p == b % q and (b % q == c % r):
            if a // p == b // q and b // q == c // r:
                print(1)
                return
    if p - a == q - b:
        print(2)
        return
    if p != 0 and q != 0 and (a % p == 0) and (a % p == b % q) and (a // p == b // q):
        print(2)
        return
    if r - c == q - b:
        print(2)
        return
    if r != 0 and q != 0 and (c % r == 0) and (c % r == b % q) and (c // r == b // q):
        print(2)
        return
    if p - a == r - c:
        print(2)
        return
    if p != 0 and r != 0 and (a % p == 0) and (a % p == c % r) and (a // p == c // r):
        print(2)
        return
    if d1d2(p, q, r, a, b, c) or d1d2(q, r, p, b, c, a) or d1d2(r, p, q, c, a, b):
        print(2)
        return
    if e1e2(p, q, r, a, b, c) or e1e2(q, r, p, b, c, a) or e1e2(r, p, q, c, a, b):
        print(2)
        return
    if d3e3(p, q, r, a, b, c):
        print(2)
        return
    if d3e2(p, q, r, a, b, c) or d3e2(q, r, p, b, c, a) or d3e2(r, p, q, c, a, b):
        print(2)
        return
    if d2e3(p, q, r, a, b, c) or d2e3(q, r, p, b, c, a) or d2e3(r, p, q, c, a, b):
        print(2)
        return
    if d2e2(p, q, r, a, b, c) or d2e2(q, r, p, b, c, a) or d2e2(r, p, q, c, a, b) or d2e2(p, r, q, a, c, b) or d2e2(q, p, r, b, a, c) or d2e2(r, q, p, c, b, a):
        print(2)
        return
    if e3d2(p, q, r, a, b, c) or e3d2(q, r, p, b, c, a) or e3d2(r, p, q, c, a, b):
        print(2)
        return
    if e2d2(p, q, r, a, b, c) or e2d2(q, r, p, b, c, a) or e2d2(r, p, q, c, a, b) or e2d2(p, r, q, a, c, b) or e2d2(q, p, r, b, a, c) or e2d2(r, q, p, c, b, a):
        print(2)
        return
    print(3)


for _ in range(int(input())):
    src = tuple(map(int, input().split()))
    dst = tuple(map(int, input().split()))
    modified(src, dst)
