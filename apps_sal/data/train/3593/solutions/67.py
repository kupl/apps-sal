def capitalize(s, ind):
    new_string = ""
    i = 0
    while i < len(s):
        if i in ind:
            new_string += s[i].upper()
        else:
            new_string += s[i]
        i += 1
    return new_string
