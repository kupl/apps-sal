def modinv(a, m):
    return pow(a, (m >> 1) - 1, m)


def c(string):
    (x, y, z) = (1, 0, 1)
    for char in string:
        (x, y, z) = (x + (x << 1), y + (y << 1) + z, z << 1) if char == 'U' else (x, y, z << 1)
    return (x, y, z)


def collatz_steps(n, steps):
    (x, y, z) = c(steps)
    p = modinv(x, z) * -y % z
    p += (n - p) // z * z
    while p < n:
        p += z
    return p
