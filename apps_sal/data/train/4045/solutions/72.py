def number(lines):
    enum_array = list(enumerate(lines, 1))
    return [f'{i}: {letter}' for (i, letter) in enum_array]
