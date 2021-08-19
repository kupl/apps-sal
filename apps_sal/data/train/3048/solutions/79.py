def alternateCase(s):
    alt = ''
    for i in s:
        if i.isupper():
            alt += i.lower()
        else:
            alt += i.upper()
    return alt
