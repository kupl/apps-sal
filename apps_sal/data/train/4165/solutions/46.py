def uni_total(string):
    if string:
        s = sum([ord(i) for i in string])
    else:
        s = 0
    return s
