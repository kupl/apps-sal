def valid_parentheses(string):
    string = [c for c in string if not c.isalpha()]
    string = ''.join(string)
    while '()' in string:
        string = string.replace('()', '')
    return True if len(string) == 0 else False
