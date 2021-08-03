def egcd(a, b):
    if a == 0:
        return 0, 1
    y, x = egcd(b % a, a)
    return x - (b // a) * y, y


def modinv(a, m):
    x, y = egcd(a, m)
    return x & (m - 1)


def c(string):
    x, y, z = 1, 0, 1
    for char in string:
        x, y, z = (x + (x << 1), y + (y << 1) + z, z << 1) if char == 'U' else (x, y, z << 1)
    return x, y, z


def collatz_steps(n, steps):
    x, y, z = c(steps)
    p = (modinv(x, z) * -y) % z
    while p < n:
        p += z
    return p
