def checkpoint1(p, q, r, a, b, c):
    if p == a and b - q == c - r:
        return True
    if q == b and a - p == c - r:
        return True
    if c == r and a - p == b - q:
        return True
    if p == a and q == b:
        return True
    if p == a and c == r:
        return True
    if c == r and b == q:
        return True
    if a - p == b - q and a - p == c - r:
        return True
    if q != 0 and r != 0 and b % q == 0 and c % r == 0 and p == a and b / q == c / r:
        return True
    if p != 0 and r != 0 and a % p == 0 and c % r == 0 and q == b and a / p == c / r:
        return True
    if p != 0 and q != 0 and a % p == 0 and b % q == 0 and c == r and a / p == b / q:
        return True
    if p != 0 and q != 0 and r != 0 and a % p == 0 and b % q == 0 and c % r == 0 and a / p == b / q and a / p == c / r:
        return True
    return False


def checkpoint2(p, q, r, a, b, c):
    x1 = a - p
    y1 = b - q
    z1 = c - r
    if p == a or q == b or r == c:
        return True
    if a - p == b - q or b - q == c - r or c - r == a - p:
        return True
    if p != 0 and q != 0 and (a % p == 0 and b % q == 0) and (a / p == b / q):
        return True
    if p != 0 and r != 0 and (a % p == 0 and c % r == 0) and (a / p == c / r):
        return True
    if q != 0 and r != 0 and (b % q == 0 and c % r == 0) and (b / q == c / r):
        return True
    if p != 0 and q != 0 and r != 0 and a % p == 0 and b % q == 0 and c % r == 0 and (a / p * b / q == c / r or a / p * c / r == b / q or b / q * c / r == a / p):
        return True
    if x1 + y1 == z1 or x1 + z1 == y1 or y1 + z1 == x1:
        return True
    if (q + x1) != 0 and r != 0 and b % (q + x1) == 0 and c % r == 0 and b / (q + x1) == c / r:
        return True
    if p != 0 and a % p == 0 and b - (q * a / p) == c - r:
        return True
    if (q + z1) != 0 and p != 0 and b % (q + z1) == 0 and a % p == 0 and b / (q + z1) == a / p:
        return True
    if r != 0 and c % r == 0 and b - (q * c / r) == a - p:
        return True
    if (p + y1) != 0 and r != 0 and a % (p + y1) == 0 and c % r == 0 and a / (p + y1) == c / r:
        return True
    if q != 0 and b % q == 0 and a - (p * b / q) == c - r:
        return True
    if (p + z1) != 0 and q != 0 and a % (p + z1) == 0 and b % q == 0 and a / (p + z1) == b / q:
        return True
    if r != 0 and c % r == 0 and a - (p * c / r) == b - q:
        return True
    if (r + y1) != 0 and p != 0 and c % (r + y1) == 0 and a % p == 0 and c / (r + y1) == a / p:
        return True
    if q != 0 and b % q == 0 and c - (r * b / q) == a - p:
        return True
    if (r + x1) != 0 and q != 0 and c % (r + x1) == 0 and b % q == 0 and c / (r + x1) == b / q:
        return True
    if p != 0 and a % p == 0 and c - (r * a / p) == b - q:
        return True
    if (p + z1) != 0 and (q + z1) != 0 and a % (p + z1) == 0 and b % (q + z1) == 0 and a / (p + z1) == b / (q + z1):
        return True
    if r != 0 and c % r == 0 and a - (p * c / r) == b - (q * c / r):
        return True
    if (p + y1) != 0 and (r + y1) != 0 and a % (p + y1) == 0 and c % (r + y1) == 0 and a / (p + y1) == c / (r + y1):
        return True
    if q != 0 and b % q == 0 and a - (p * b / q) == c - (r * b / q):
        return True
    if (q + x1) != 0 and (r + x1) != 0 and b % (q + x1) == 0 and c % (r + x1) == 0 and b / (q + x1) == c / (r + x1):
        return True
    if p != 0 and a % p == 0 and b - (q * a / p) == c - (r * a / p):
        return True
    if r != 0 and c % r == 0 and c / r != 0 and a % (c / r) == 0 and b % (c / r) == 0 and a / (c / r) - p == b / (c / r) - q:
        return True
    if p != 0 and q != 0 and (a - z1) % p == 0 and (b - z1) % q == 0 and (a - z1) / p == (b - z1) / q:
        return True
    if q != 0 and b % q == 0 and b / q != 0 and a % (b / q) == 0 and c % (b / q) == 0 and a / (b / q) - p == c / (b / q) - r:
        return True
    if p != 0 and r != 0 and (a - y1) % p == 0 and (c - y1) % r == 0 and (a - y1) / p == (c - y1) / r:
        return True
    if p != 0 and a % p == 0 and a / p != 0 and b % (a / p) == 0 and c % (a / p) == 0 and b / (a / p) - q == c / (a / p) - r:
        return True
    if q != 0 and r != 0 and (b - x1) % q == 0 and (c - x1) % r == 0 and (b - x1) / q == (c - x1) / r:
        return True
    if (q - p) != 0 and (r - q) != 0 and (b - a) % (q - p) == 0 and (c - b) % (r - q) == 0 and (b - a) / (q - p) == (c - b) / (r - q):
        return True
    return False


test = int(input())
for _ in range(test):
    x1, y1, z1 = [int(x) for x in input().split()]
    a, b, c = [int(x) for x in input().split()]
    if a == x1 and b == y1 and c == z1:
        print(0)
    elif checkpoint1(x1, y1, z1, a, b, c):
        print(1)
    elif checkpoint2(x1, y1, z1, a, b, c):
        print(2)
    else:
        print(3)
