def rotate(n, s):
    if not s: return s
    n = -n % len(s)
    return s[n:] + s[:n]

def cipher(n, s):
    sp = [i for i, c in enumerate(s) if c == ' '] + [len(s)]
    s = s.split(' ')
    if n < 0: s = [rotate(n, w) for w in s]
    s = rotate(n, ''.join(s))
    s = [s[i+1-x: j-x] for x, (i, j) in enumerate(zip([-1] + sp, sp))]
    if n > 0: s = [rotate(n, w) for w in s]
    return ' '.join(s)

def encode(n, s):
    for _ in range(n): s = cipher(n, s)
    return f'{n} {s}'

def decode(s):
    n, s = s.split(' ', 1)
    n = int(n)
    for _ in range(n): s = cipher(-n, s)
    return s
