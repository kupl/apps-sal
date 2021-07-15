def capitalize(s):
    list = []
    ret = ""
    i = True  # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    list.append(ret)
    ret2 = ret.swapcase()
    list.append(ret2)
    return list
