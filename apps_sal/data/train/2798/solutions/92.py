def to_alternating_case(string):
    ret = []
    for char in string:
        if char.isupper():
            ret.append(char.lower())
        else:
            ret.append(char.upper())
    return ''.join(ret)
