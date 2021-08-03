def number(lines):
    x = 1
    for i in range(len(lines)):
        lines[i] = str(x) + ": " + lines[i]
        x += 1
    return lines
