def solve(s):
    words = s.split()
    cure = ''.join(words)[::-1]
    r = 0
    krum = []
    for i in words:
        krum.append(cure[r:r + len(i)])
        r = r + len(i)
    return ' '.join(krum) if s[len(s) - 1] != ' ' else ' '.join(krum) + ' '
