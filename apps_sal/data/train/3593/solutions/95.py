def capitalize(s, ind):
    st = ''
    for (index, value) in enumerate(s):
        if index in ind:
            st += s[index].upper()
        else:
            st += s[index]
    return st
