def capitalize(s):
    ret = [''] * 2
    for i in range(len(s)):
        ret[i % 2] += s[i].upper()
        ret[(i + 1) % 2] += s[i]
    return ret
