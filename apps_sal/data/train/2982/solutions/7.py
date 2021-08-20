def pascal(p):
    l = [[1]]
    for index in range(p - 1):
        values = []
        for (i, j) in enumerate(l[index][:-1]):
            values.append(j + l[index][i + 1])
        l.append(l[index][:1] + values + l[index][-1:])
    return l
