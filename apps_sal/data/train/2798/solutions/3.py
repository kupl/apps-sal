def to_alternating_case(string):
    strn = ''
    for i in string:
        if i.isupper():
            strn += i.lower()
        else:
            strn += i.upper()
    return strn
