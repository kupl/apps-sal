def shortest_to_char(s, c):
    L = [i for i, x in enumerate(s) if x == c]
    return [min(abs(i - j) for j in L) for i, x in enumerate(s)] if L else []
