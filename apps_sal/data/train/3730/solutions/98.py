def capitalize(s):
    s1 = ""
    s2 = ""
    index = 0
    k = 0
    l = []
    for i in s:
        if index % 2 == 0:
            s1 += i.upper()
        else:
            s1 += i
        index += 1
    for j in s:
        if k % 2 != 0:
            s2 += j.upper()
        else:
            s2 += j
        k += 1
    l.append(s1)
    l.append(s2)
    return l
