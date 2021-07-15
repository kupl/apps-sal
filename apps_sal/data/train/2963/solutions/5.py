def swap(string_):
    s = ''
    for i in string_:
        if i.isupper():
            s += i.lower()
        else:
            s += i.upper()
    return s
