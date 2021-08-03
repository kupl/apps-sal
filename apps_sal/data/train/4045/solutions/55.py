def number(lines):
    output = []
    for i, v in enumerate(lines, 1):
        output.append(str(i) + ': ' + str(v))
    return output
