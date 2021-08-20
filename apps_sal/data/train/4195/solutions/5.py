def merge(line):
    if line[0] != 0 and line[0] == line[1]:
        if line[2] != 0 and line[2] == line[3]:
            return [line[0] + line[1], line[2] + line[3], 0, 0]
        else:
            return [line[0] + line[1], line[2], line[3], 0]
    elif line[0] != 0 and line[1] == 0 and (line[0] == line[2]):
        return [line[0] + line[2], line[3], 0, 0]
    elif line[0] != 0 and line[1] == 0 and (line[2] == 0) and (line[0] == line[3]):
        return [line[0] + line[3], 0, 0, 0]
    elif line[0] != 0:
        if line[1] != 0 and line[1] == line[2]:
            return [line[0], line[1] + line[2], line[3], 0]
        elif line[1] != 0 and line[2] == 0 and (line[1] == line[3]):
            return [line[0], line[1] + line[3], 0, 0]
        elif line[1] != 0:
            if line[2] != 0 and line[2] == line[3]:
                return [line[0], line[1], line[2] + line[3], 0]
            else:
                return [line[0], line[1], line[2], line[3]]
        elif line[2] != 0 and line[2] == line[3]:
            return [line[0], line[2] + line[3], 0, 0]
        else:
            return [line[0], line[2], line[3], 0]
    elif line[1] != 0 and line[1] == line[2]:
        return [line[1] + line[2], line[3], 0, 0]
    elif line[1] != 0 and line[2] == 0 and (line[1] == line[3]):
        return [line[1] + line[3], 0, 0, 0]
    elif line[1] != 0:
        if line[2] != 0 and line[2] == line[3]:
            return [line[1], line[2] + line[3], 0, 0]
        else:
            return [line[1], line[2], line[3], 0]
    elif line[2] != 0 and line[2] == line[3]:
        return [line[2] + line[3], 0, 0, 0]
    else:
        return [line[2], line[3], 0, 0]


def merge(line):
    (i, res) = (0, [])
    while i < len(line):
        x = line[i]
        if x:
            for (j, y) in enumerate(line[i + 1:], 1):
                if y:
                    if x == y:
                        res.append(x + y)
                        i += j
                    else:
                        res.append(x)
                    break
            else:
                res.append(x)
        i += 1
    return res + [0] * (len(line) - len(res))
