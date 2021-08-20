def bracket_pairs(string):
    opened = []
    result = {}
    for (i, ch) in enumerate(string):
        if ch == '(':
            opened.append((ch, i))
        elif ch == ')':
            if not opened:
                return False
            result[opened[-1][1]] = i
            opened = opened[:-1]
    return False if opened else result
