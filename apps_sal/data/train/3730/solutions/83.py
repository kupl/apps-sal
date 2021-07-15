def capitalize(s):
    x = []
    b = ''
    for i in range(len(s)):
        if i %2==0:
            c = s[i].upper()
            b += c
        else:
            c = s[i].lower()
            b += c
    x.append(b)
    d = b.swapcase()
    x.append(d)
    return x
