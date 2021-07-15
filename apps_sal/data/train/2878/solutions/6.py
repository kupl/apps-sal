def shortest_to_char(s, c):
    if not (s and c and c in s):
        return []
    idxs = [i for i, x in enumerate(s) if x == c]
    return [min(abs(j-i) for j in idxs) for i, x in enumerate(s)]
