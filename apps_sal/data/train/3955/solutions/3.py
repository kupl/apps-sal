def bracket_pairs(s):
    a, d = [], {}
    for i, x in enumerate(s):
        if x == "(":
            a.append(i)
        if x == ")":
            if not a:
                return 0
            d[a.pop()] = i
    return not a and d
