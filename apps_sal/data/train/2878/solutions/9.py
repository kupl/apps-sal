def shortest_to_char(s, c):
    if not c in s or not c: return []
    return [(0 if c == s[x] else min([abs(x - y) for y in [x for x in range(len(s)) if s[x] == c]])) for x in range(len(s))]

