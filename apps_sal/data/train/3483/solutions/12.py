def string_parse(string):
    if not isinstance(string, str):
        return 'Please enter a valid string'
    res = []
    count = 0
    last_char = None
    for c in string:
        if c != last_char:
            if count > 2:
                res.append(']')
            count = 0
        elif count == 2:
            res.append('[')
        count += 1
        last_char = c
        res.append(c)
    if count > 2:
        res.append(']')
    return ''.join(res)
