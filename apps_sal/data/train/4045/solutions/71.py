def number(lines):
    if lines != [] or None:
        for i in range(len(lines)):
            lines[i] = str(i + 1) + ': ' + lines[i]
        return lines
    else:
        return []
