def solve(a, b):
    if a == b:
        return True
    if '*' not in a:
        return False
    sides = a.split('*')
    missing = b[len(sides[0]):len(b) - len(sides[1])]
    c = a.replace('*', missing)
    return c == b
