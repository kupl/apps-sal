def alternateCase(s):
    new_s = ''
    for ltr in s:
        if ltr.lower() == ltr:
            ltr = ltr.upper()
        else:
            ltr = ltr.lower()
        new_s += ltr
    return new_s
