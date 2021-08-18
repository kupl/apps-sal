def to_alternating_case(s):
    """(^-__-^)"""
    new_line = ""
    for a in s:
        if a.isupper():
            new_line += a.lower()
        elif a.islower():
            new_line += a.upper()
        else:
            new_line += a
    return new_line
