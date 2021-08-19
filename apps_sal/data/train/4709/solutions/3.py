def sequence(n):
    return n and 3 * sequence(n >> 1) + (n & 1)
