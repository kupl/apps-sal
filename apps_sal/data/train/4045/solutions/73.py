def number(lines):
    lines = [] if lines == [] else [(str(i + 1) + ": " + str(lines[i])) for i in range(len(lines))]
    return lines
