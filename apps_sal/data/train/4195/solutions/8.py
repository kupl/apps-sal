def merge(line):
    temp = [x for x in line if x != 0]
    res = []
    while temp:
        if len(temp) > 1 and temp[0] == temp[1]:
            res.append(temp.pop(0) + temp.pop(0))
        else:
            res.append(temp.pop(0))
    return res + [0] * (len(line) - len(res))
