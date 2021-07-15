def validBraces(string):
    while '()' in string or '{}' in string or '[]' in string:
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
    return False if len(string) != 0 else True
