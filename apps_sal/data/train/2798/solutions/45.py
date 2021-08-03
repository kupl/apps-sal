def to_alternating_case(string):
    result = ''
    for c in string:
        if c == c.upper():
            result = result + c.lower()
        else:
            result = result + c.upper()
    return result
