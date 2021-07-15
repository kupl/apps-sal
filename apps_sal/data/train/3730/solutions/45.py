def capitalize(s):
    ret = ""
    ter  = ""
    i = True   
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    i = True
    for char in s:
        if not i:
            ter += char.upper()
        else:
            ter += char.lower()
        if char != ' ':
            i = not i
    return [ret,ter]
