def rotate(l, n):
    return l[len(l) - (n % len(l) + len(l)) % len(l):] + l[:len(l) - (n % len(l) + len(l)) % len(l)]
