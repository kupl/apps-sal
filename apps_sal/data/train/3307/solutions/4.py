def fat_fingers(string):
    if type(string) != str: return string
    aCnt, chars = 0, []
    for c in string:
        if c in 'aA': aCnt += 1
        else:         chars.append(c.swapcase()) if aCnt&1 else chars.append(c) 
    return ''.join(chars)

