def capitalize(s,ind):
    a=''
    for i in range(len(s)):
        if i in ind:
            a+=s[i].upper()
        else:
            a+=s[i]
    return a
