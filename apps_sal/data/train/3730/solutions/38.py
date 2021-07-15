def capitalize(s):
    st = ""
    st1 = ""
    for i in range(len(s)):
        if i % 2 == 0:
            st += s[i].upper()
            st1 += s[i].lower()
        else:
            st1 += s[i].upper()
            st += s[i].lower()
    return [st, st1]
