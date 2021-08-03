def number(lines):
    for i in range(len(lines)):
        n = i + 1
        n = str(n)
        s = str(lines[i])
        lines[i] = n + ":" + " " + s
        n = int(n)
    return lines
