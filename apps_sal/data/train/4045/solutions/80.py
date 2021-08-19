def number(lines):
    output = []
    char = 1
    for n in lines:
        output.append(str(char) + ': ' + n)
        char += 1
    return output
