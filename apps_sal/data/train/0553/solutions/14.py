def aa22(p, q, r, a, b, c):
    if q + a - p + c - r == b:
        return 1
    else:
        return 0


def aa21(p, q, r, a, b, c):
    if p - q == a - b:
        return 1
    else:
        return 0


def as22(p, q, r, a, b, c):
    if p + b - c + r - q == a:
        return 1
    else:
        return 0


def am22(p, q, r, a, b, c):
    if r != 0 and c != 0 and (c % r == 0) and (b * r % c == 0) and (b * r // c - q == a - p):
        return 1
    else:
        return 0


def am21(p, q, r, a, b, c):
    if r != 0 and c % r == 0 and (p - q == a - b):
        return 1
    else:
        return 0


def am23(p, q, r, a, b, c):
    if r != 0 and c != 0 and (c % r == 0) and (b * r % c == 0) and (a * r % c == 0) and (a * r // c - p == b * r // c - q):
        return 1
    else:
        return 0


def am32(p, q, r, a, b, c):
    if q + c - r != 0 and p + c - r != 0 and (b // (q + c - r) == a // (p + c - r)) and (b % (q + c - r) == 0) and (a % (p + c - r) == 0):
        return 1
    else:
        return 0


def ma33(p, q, r, a, b, c):
    if p - q != 0 and (b * p - a * q) % (p - q) == 0 and (q - r != 0) and (p != 0) and ((c * q - b * r) % (q - r) == 0) and ((b * p - a * q) // (p - q) == (c * q - b * r) // (q - r)) and ((a - (b * p - a * q) // (p - q)) % p == 0):
        return 1
    else:
        return 0


def am33(p, q, r, a, b, c):
    if a - b != 0 and (b * p - a * q) % (a - b) == 0 and (b - c != 0) and ((c * q - b * r) % (b - c) == 0) and ((b * p - a * q) // (a - b) == (c * q - b * r) // (b - c)) and (p + (b * p - a * q) // (a - b) != 0) and (a % (p + (b * p - a * q) // (a - b)) == 0):
        return 1
    else:
        return 0


def ma22(p, q, r, a, b, c):
    if p != 0 and q != 0 and (a % p == 0) and ((b - c + r) % q == 0) and (a // p == (b - c + r) // q):
        return 1
    else:
        return 0


def ma21(p, q, r, a, b, c):
    if p != 0 and q != 0 and (a % p == 0) and (b % q == 0) and (a // p == b // q):
        return 1
    else:
        return 0


def ma23(p, q, r, a, b, c):
    if q != 0 and p != 0 and ((b - c + r) % q == 0) and ((a - c + r) % p == 0) and ((b - c + r) // q == (a - c + r) // p):
        return 1
    else:
        return 0


def ma32(p, q, r, a, b, c):
    if r != 0 and q * c % r == 0 and (p * c % r == 0) and (b - q * c // r == a - p * c // r) and (c % r == 0):
        return 1
    else:
        return 0


def ms22(p, q, r, a, b, c):
    if q != 0 and p != 0 and ((b + r - c) % q == 0) and (a % p == 0) and ((b + r - c) // q == a // p):
        return 1
    else:
        return 0


def mm22(p, q, r, a, b, c):
    if q * c != 0 and b * r % (q * c) == 0 and (p != 0) and (a % p == 0) and (a // p == b * r // (q * c)):
        return 1
    else:
        return 0


def mm21(p, q, r, a, b, c):
    if r != 0 and c % r == 0 and (q != 0) and (p != 0) and (b // q == a // p) and (b % q == 0) and (a % p == 0):
        return 1
    else:
        return 0


def sa22(p, q, r, a, b, c):
    if q - b + c - r == p - a:
        return 1
    else:
        return 0


def sa21(p, q, r, a, b, c):
    if p - a == q - b:
        return 1
    else:
        return 0


def sm32(p, q, r, a, b, c):
    if q - r + c != 0 and p - r + c != 0 and (b // (q - r + c) == a // (p - r + c)) and (b % (q - r + c) == 0) and (a % (p - r + c) == 0):
        return 1
    else:
        return 0


def as2(q, r, b, c):
    if q - r == b - c:
        return 1
    else:
        return 0


def m2(q, r, b, c):
    if r != 0 and q != 0 and (b // q == c // r) and (b % q == 0) and (c % r == 0):
        return 1
    else:
        return 0


def as3(p, q, r, a, b, c):
    if p - q == a - b and q - r == b - c and (p - r == a - c):
        return 1
    else:
        return 0


def m3(p, q, r, a, b, c):
    if q != 0 and r != 0 and (p != 0) and (a // p == b // q) and (b // q == c // r) and (a % p == 0) and (b % q == 0) and (c % r == 0):
        return 1
    else:
        return 0


t = int(input())
while t > 0:
    (p, q, r) = map(int, input().split())
    (a, b, c) = map(int, input().split())
    l = []
    d = []
    l3 = []
    l.append(p)
    l.append(q)
    l.append(r)
    l.append(p)
    l.append(r)
    l.append(q)
    l.append(q)
    l.append(p)
    l.append(r)
    l.append(q)
    l.append(r)
    l.append(p)
    l.append(r)
    l.append(p)
    l.append(q)
    l.append(r)
    l.append(q)
    l.append(p)
    l3.append(a)
    l3.append(b)
    l3.append(c)
    l3.append(a)
    l3.append(c)
    l3.append(b)
    l3.append(b)
    l3.append(a)
    l3.append(c)
    l3.append(b)
    l3.append(c)
    l3.append(a)
    l3.append(c)
    l3.append(a)
    l3.append(b)
    l3.append(c)
    l3.append(b)
    l3.append(a)
    l2 = []
    l4 = []
    if p == a:
        l2.append(q)
        l2.append(r)
        l4.append(b)
        l4.append(c)
    if q == b:
        l2.append(p)
        l2.append(r)
        l4.append(a)
        l4.append(c)
    if r == c:
        l2.append(p)
        l2.append(q)
        l4.append(a)
        l4.append(b)
    sol = 0
    ans = 0
    cnt = (p == a) + (q == b) + (r == c)
    if p == a and q == b and (r == c):
        ans = 4
    elif cnt == 2:
        ans = 1
    elif cnt == 1:
        for i in range(0, 2, 2):
            sol = as2(l2[i], l2[i + 1], l4[i], l4[i + 1])
            if sol == 1:
                break
            sol = m2(l2[i], l2[i + 1], l4[i], l4[i + 1])
            if sol == 1:
                break
        if sol == 1:
            ans = 1
            sol = 0
        else:
            ans = 2
    elif cnt == 0 and ans == 0:
        sol = as3(p, q, r, a, b, c)
        if sol == 1:
            ans = 1
        sol = m3(p, q, r, a, b, c)
        if sol == 1:
            ans = 1
    sol = 0
    for i in range(0, 16, 3):
        if ans != 0:
            break
        sol = aa22(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = aa21(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = as22(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = am22(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = am21(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = am23(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = am32(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = ma33(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = am33(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = ma22(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = ma21(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = ma23(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = ma32(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = ms22(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = mm22(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = mm21(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = sa22(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
        sol = sm32(l[i], l[i + 1], l[i + 2], l3[i], l3[i + 1], l3[i + 2])
        if sol == 1:
            break
    if sol == 1 and ans == 0:
        ans = 2
    elif ans == 0 and sol != 1:
        ans = 3
    if ans == 4:
        print('0')
    else:
        print(ans)
    t = t - 1
