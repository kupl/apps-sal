def solve(a, b):
    p = 2
    while True:
        if b == 1:
            return True
        if a % p > 0 and b % p == 0:
            return False
        while b % p == 0:
            b /= p
        p += 1
