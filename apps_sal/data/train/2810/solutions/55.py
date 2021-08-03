def solve(a):
    t = [chr(x + 96) for x in range(1, 27)]
    return [sum([x.lower()[y] == t[y] for y in range(min(len(x), 26))]) for x in a]
