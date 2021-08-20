def largest_arrangement(a):
    return (lambda l: int(''.join(sorted(map(str, a), key=lambda s: s.ljust(l, s[0]))[::-1])))(len(str(max(a))))
