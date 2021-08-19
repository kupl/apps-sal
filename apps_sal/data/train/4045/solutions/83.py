def number(lines):
    result = []
    for (i, j) in enumerate(lines):
        result.append(str(i + 1) + ': ' + str(j))
    return result
