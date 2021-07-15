def doubles(s):
    chars = set(s)
    while True: 
        token = s
        for c in chars: 
            s = s.replace(c+c, '')
        if len(token) == len(s): 
            break
    return s
