def bracket_pairs(string):
    (ob, res) = ([], {})
    for (n, e) in enumerate(string):
        if e == '(':
            ob.append(n)
        elif e == ')':
            if not ob:
                return False
            res[ob.pop()] = n
    return False if ob else res
