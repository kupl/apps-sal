def hex_color(s):
    (a, b, c) = [int(x) for x in s.split() or [0, 0, 0]]
    for (n, r) in [(0, 'black'), (c, 'white')]:
        if a == b == c == n:
            return r
    m = max(a, b, c)
    if m == a == b:
        return 'yellow'
    if m == a == c:
        return 'magenta'
    if m == b == c:
        return 'cyan'
    return 'red' if m == a else 'green' if m == b else 'blue'
