def multiple_split(string, delimiters=[]):
    print(string, delimiters)
    if not string:
        return []  # trivial case
    if not delimiters:
        return [string]  # trivial case
    for d in delimiters[1:]:
        string = string.replace(d, delimiters[0])
    tokens = string.split(delimiters[0])
    return [t for t in tokens if t]
