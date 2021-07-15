def number(lines):
    for i in lines:
        lines[lines.index(i)] = '{0}: {1}'.format(lines.index(i) + 1, i)
    return lines
