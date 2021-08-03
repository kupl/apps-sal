def solve(a, b):
    s, n = 0, 0
    for x, y in zip(a, b):
        if x > y:
            n += 1
        elif x < y:
            s += 1
    if s != n:
        return f'{n}, {s}: {"Alice" if s<n else "Bob"} made "{"Kurt" if s<n else "Jeff"}" proud!'
    return f'{n}, {s}: that looks like a "draw"! Rock on!'
