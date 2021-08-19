def bracket_pairs(stg):
    (open, dic) = ([], {})
    for (i, e) in enumerate(stg):
        if e == '(':
            open.append(i)
        if e == ')':
            if not open:
                return False
            dic[open.pop(-1)] = i
    return False if open else dic
