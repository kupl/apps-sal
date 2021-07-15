def to_alternating_case(string):
    a = ''
    for n in string:
        if n.isupper():
            a += n.lower()
        elif n.islower():
            a += n.upper()
        else:
            a += n
    return a
