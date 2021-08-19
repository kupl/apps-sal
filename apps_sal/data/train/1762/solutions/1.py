d = {'L': 1, 'R': -1}


def mouse_path(s):
    if invalid(s):
        return None
    area, x = 0, 0
    while True:
        g = (i for i, c in enumerate(s) if c in d)
        i, j = next(g, -1), next(g, -1)
        area += x * int(s[:i])
        if j == -1:
            break
        x = d[s[j]] * (int(s[i + 1:j]) - d[s[i]] * x)
        s = s[j + 1:]
    return abs(area)


def invalid(s):  # Checks if the path is invalid
    x, y, sgn = 0, 0, 1
    V, H = [], []
    while True:
        g = (i for i, c in enumerate(s) if c in d)
        i, j = next(g, -1), next(g, -1)
        if i == -1:
            return True
        a, b = sgn * int(s[:i]), d[s[i]] * sgn * int(s[i + 1:] if j == -1 else s[i + 1:j])
        H.append((x, y, a))
        for p, q, r in V[:-1]:
            if (y - q)**2 <= (y - q) * r and (p - x)**2 <= (p - x) * a:
                return True
        V.append((x + a, y, b))
        for p, q, r in H[1:-1] if j == -1 else H[:-1]:
            if (q - y)**2 <= (q - y) * b and (x + a - p)**2 <= (x + a - p) * r:
                return True
        x, y = x + a, y + b
        if j == -1:
            break
        sgn *= -d[s[i]] * d[s[j]]
        s = s[j + 1:]
    return x != 0 or y != 0
