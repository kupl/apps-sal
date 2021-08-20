def number(lines):
    new_lines = []
    for (i, ele) in enumerate(lines):
        new_lines.append(str(i + 1) + ': ' + ele)
    return new_lines
