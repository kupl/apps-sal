def number(lines):
    r = []
    n = 1
    for s in lines:
        r.append(str(n) + ': '+ s)
        n +=1
    return r
