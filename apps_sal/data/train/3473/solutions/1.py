def doubles(s):
    for i in s:
        if i*2 in s:
            
            s = s.replace(i*2, '')
    return s
