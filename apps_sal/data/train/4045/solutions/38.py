def number(lines):

    out = []
    for i in range(len(lines)):
        out.append('{}: {}'.format(i + 1, lines[i]))

    return out
