def capitalize(s):
    a = ""
    big = True
    for i in s:
        if big == True:
            i = i.upper()
            big = False
        else:
            big = True
        a += i
    b = ""
    big = False
    for i in s:
        if big == True:
            i = i.upper()
            big = False
        else:
            big = True
        b += i
    return [a, b]
