def multiple_split(string, delimiters=[]):
    if delimiters == []:
        return [string] if string else []
    for deli in delimiters:
        string = ' '.join(string.split(deli))
    string = string.split(' ')
    return list(filter(None, string))
