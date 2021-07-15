def capitalize(s):
    vars = []
    for num in range(2):
        buf = ''
        for ind in range(len(s)):
            if ind % 2 == num:
                buf += s[ind].upper()
            else:
                buf += s[ind]
        vars.append(buf)
    return vars
