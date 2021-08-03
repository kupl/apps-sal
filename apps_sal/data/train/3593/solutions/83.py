def capitalize(s, ind):
    output = ''
    for i in range(len(s)):
        if i in ind:
            if i < len(s):
                output += s[i].upper()
        else:
            output += s[i]
    return output
