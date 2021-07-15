def compare(s1,s2):
    r1 = r2 = 0
    if s1: 
        for c in s1:
            if not c.isalpha():
                r1 = 0
                break
            r1 += ord(c.upper())
    if s2:   
        for c in s2:
            if not c.isalpha():
                r2 = 0
                break
            r2 += ord(c.upper())   
    return r1 == r2
