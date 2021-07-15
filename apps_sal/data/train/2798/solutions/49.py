def to_alternating_case(string):
    out = ''
    for i in string:
        if i.isupper():
            out = out + i.lower()
        else:
            out = out + i.upper()
            
    return out
