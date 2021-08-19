def repeat_adjacent(string):
    (a, b, c, d) = (0, [], '', 0)
    for i in range(a, len(string) - 1):
        if string[i] == string[i + 1]:
            continue
        else:
            b.append(string[a:i + 1])
            a = i + 1
    b.append(string[-(len(string) - a):])
    for j in b:
        if len(j) > 1:
            c += j
        else:
            c += '*'
    for k in c.split('*'):
        if len(set(k)) > 1:
            d += 1
    return d
