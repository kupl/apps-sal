def capitalize(s,ind):
    ret = ''
    for i, letter in enumerate(s):
        if i in ind:
            ret += letter.upper()
        else:
            ret += letter
    return ret
