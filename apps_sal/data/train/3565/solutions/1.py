def solve(s, k):
    return ''.join((t[1] for t in sorted(sorted(enumerate(s), key=lambda x: x[1])[k:])))
