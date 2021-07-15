def sc(s):
    list_s = []
    for i in s:
        if i.lower() in s and i.upper() in s:
            list_s.append(i)
    return ''.join(list_s)

