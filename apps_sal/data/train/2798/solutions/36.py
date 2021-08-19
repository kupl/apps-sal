def to_alternating_case(string):
    strn = ''
    for i in string:
        if i == i.upper():
            strn += i.lower()
        elif i == i.lower():
            strn += i.upper()
    return strn
