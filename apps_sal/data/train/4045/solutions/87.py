def number(lines):
    n = 0
    l = []
    for i in lines:
        n += 1
        l.append(str(n) +': '+ i)
    return l
