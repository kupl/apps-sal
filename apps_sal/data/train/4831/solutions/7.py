def solved(string):
    l = len(string)
    if l % 2 == 1:
        string = string[0:l // 2] + string[1 + l // 2:]
    return ''.join(sorted(string))
