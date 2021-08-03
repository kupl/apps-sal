def number(lines):
    i = 0

    if lines == []:
        return []
    else:
        while i < len(lines):
            lines[i] = (str(i + 1) + ': ' + lines[i])
            i = i + 1
    return (lines)
