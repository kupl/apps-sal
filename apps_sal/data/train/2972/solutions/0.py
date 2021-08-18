def multiple_split(string, delimiters=[]):
    for d in delimiters:
        string = string.replace(d, '
    return [s for s in string.split('
