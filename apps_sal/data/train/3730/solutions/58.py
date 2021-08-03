def capitalize(s):
    lst = ["", ""]
    for i in range(0, len(s)):
        if i % 2 == 0:
            lst[0] += s[i].upper()
            lst[1] += s[i]
        else:
            lst[1] += s[i].upper()
            lst[0] += s[i]
    return lst
