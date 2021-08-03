def number(lines):
    s = []
    [s.append(str(i + 1) + ': ' + lines[i])for i in range(len(lines))]
    return s
