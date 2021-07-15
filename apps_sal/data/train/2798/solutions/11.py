def to_alternating_case(string):
    res = ''
    for c in string:
        res += c.upper() if c.islower() else c.lower()
    return res
