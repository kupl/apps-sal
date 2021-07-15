def alternateCase(s):
    k = ''
    for i in s:
        if i.islower():
            k += i.upper()
        elif i.isupper():
            k += i.lower()
        else:
            k += i
    return k
