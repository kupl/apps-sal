def to_alternating_case(string):
    a = ''
    for i in string:
        if i == i.upper():
            a += i.lower()
        else:
            a += i.upper()
    return a
