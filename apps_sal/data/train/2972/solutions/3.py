def multiple_split(string, delimiters=[]):
    print(string, delimiters)
    if not string:
        return []
    if not delimiters:
        return [string]
    for d in delimiters[1:]:
        string = string.replace(d, delimiters[0])
    tokens = string.split(delimiters[0])
    return [t for t in tokens if t]
