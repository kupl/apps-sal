def shortest_to_char(s, c):
    return [min((x.find(c) + 1 or 1000.0 for x in [s[i:], s[:i + 1][::-1]])) - 1 for i in range(len(s))] if c and c in s else []
