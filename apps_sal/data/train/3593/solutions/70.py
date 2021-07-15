def capitalize(s,ind):
    new_string = ''
    for i in range(len(s)):
        if i in ind:
            new_string += s[i].upper()
        else:
            new_string += s[i]
    return new_string
