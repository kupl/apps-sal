import random
import os
yash = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997)


def fix(m):
    for ai in yash:
        if m % ai == 0:
            return ai
    return m


def rabin_miller(a, i, n):
    if i == 0:
        return 1
    x = rabin_miller(a, i / 2, n)
    if x == 0:
        return 0
    y = x * x % n
    if y == 1 and x != 1 and (x != n - 1):
        return 0
    if i % 2 != 0:
        y = a * y % n
    return y


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def brent_rho(n):
    if n <= 3 or rabin_miller(random.randint(2, n - 2), n - 1, n) == 1:
        return n
    (y, r, q, m) = (1, 1, 1, 203)
    while 1:
        x = y
        for i in range(1, r + 1):
            y = (y * y + 1) % n
        k = 0
        while 1:
            ys = y
            for i in range(1, min(m, r - k) + 1):
                y = (y * y + 1) % n
                q = q * abs(x - y) % n
            g = gcd(q, n)
            k += m
            if k >= r or g > 1:
                break
        r *= 2
        if g > 1:
            break
    if g == n:
        while 1:
            ys = (ys * ys + 1) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break
    if g == n:
        return n
    return brent_rho(g)


def divsum2(n):
    if n == 1:
        return 0
    d = brent_rho(n)
    d = fix(d)
    assert d <= 3 or rabin_miller(random.randint(2, d - 2), d - 1, d) == 1
    (f, m) = (0, n)
    while m % d == 0:
        m /= d
        f = f + 1
    return f * d + divsum2(m)


try:
    while 1:
        z = eval(input())
        print(divsum2(z))
except:
    os.sys.exit(0)
