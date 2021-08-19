def merge(line):
    line = ungap(line)
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            (line[i], line[i + 1], i) = (line[i] * 2, 0, i + 1)
    return ungap(line)


def ungap(line):
    return [n for n in line if n] + [0] * line.count(0)
