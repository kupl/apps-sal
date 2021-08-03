def alternateCase(s):
    k = ""
    for x in s:
        if x in "qwertyuioplkjhgfdsazxcvbnm":
            k = k + x.upper()
        elif x in "QWERTYUIOPASDFGHJKLZXCVBNM":
            k = k + x.lower()
        else:
            k = k + x

    return k
