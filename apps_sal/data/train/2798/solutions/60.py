def to_alternating_case(string):
    str2 = ''
    for c in string:
        if c.isupper():
            str2 += c.lower()
        elif c.islower():
            str2 += c.upper()
        else:
            str2 += c
    return str2
