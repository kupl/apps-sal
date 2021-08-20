def bracket_pairs(string):
    (res, open) = ({}, [])
    for (i, c) in enumerate(string):
        if c == '(':
            open.append(i)
        if c == ')':
            try:
                res[open.pop()] = i
            except IndexError:
                return False
    return not open and res
