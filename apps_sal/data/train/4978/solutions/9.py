def rotate(n, s):
    i = -n % len(s) if len(s) > 0 else 1
    return s[i:] + s[:i]


def cipher(n, s):
    sp = [i for i, c in enumerate(s) if c == " "] + [len(s)]
    s = s.split(' ')
    if n < 0:
        s = [rotate(n, w) for w in s]
    s = rotate(n, ''.join(s))
    s = [s[i + 1 - x:j - x] for x, (i, j) in enumerate(zip([-1] + sp, sp))]
    if n > 0:
        s = [rotate(n, w) for w in s]
    return ' '.join(s)


def encode(n, strng):
    s = strng
    for _ in range(n):
        s = cipher(n, s)
    return "{} {}".format(n, s)


def decode(strng):
    n, s = strng.split(" ", 1)
    n = int(n)
    for _ in range(n):
        s = cipher(-n, s)
    return s
