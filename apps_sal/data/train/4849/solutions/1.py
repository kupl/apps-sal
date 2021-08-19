def my_very_own_split(string, delimiter=None):
    if delimiter == '':
        raise ValueError
    if delimiter is None:
        string = string.replace('\t', ' ')
        while '  ' in string:
            string = string.replace('  ', ' ')
        delimiter = ' '
    (last, l) = (0, len(delimiter))
    for i in range(len(string)):
        if string[i:i + l] == delimiter:
            yield string[last:i]
            last = i + l
    yield string[last:]
