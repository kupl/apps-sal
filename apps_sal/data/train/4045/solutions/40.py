def number(lines):
    index = 0
    for line in lines:
        lines[index] = str(index+1) + ": " + line
        index += 1
    return lines
