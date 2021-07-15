def to_alternating_case(string):
    res = ""
    for l in string:
        if l.isupper():
            l = l.lower()
            res += l
        elif l.islower():
            l = l.upper()
            res += l
        else: res += l
    return res
