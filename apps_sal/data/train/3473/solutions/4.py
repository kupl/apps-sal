def doubles(s):
    for x in range(0,3):
        for a in "abcdefghijklmnopqrstuvwqxyz": s=s.replace(2*a,"")
    return s
