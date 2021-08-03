def solve(n):
    def inversion(s, a, b):
        x, y = s.rfind(a), s.rfind(b)
        if a == b:
            x = s.rfind(a, 0, y)
        # Suffix not found
        if not x > -1 < y:
            return float('inf')
        inv = len(s) - 2 - x + len(s) - 1 - y + (x > y)
        # Leading zeros
        if not x > 0 < y:
            t = s[1 + ({x, y} == {0, 1}): ]
            if t:
                inv += len(s) - len(str(int(t))) - 1 - ({x, y} == {0, 1})
        return inv

    inv = min(inversion(str(n), a, b) for a, b in '00 25 50 75'.split())
    return -1 if inv == float('inf') else inv
