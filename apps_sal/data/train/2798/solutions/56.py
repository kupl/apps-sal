def to_alternating_case(string):
    out = ""
    for s in string:
        if s.islower():
            out += s.upper()
        elif s.isupper():
            out += s.lower()
        else:
            out += s
            
    return out
