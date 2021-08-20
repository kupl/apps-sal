def valid_parentheses(string):
    string = ''.join((ch for ch in string if ch in '()'))
    while '()' in string:
        string = string.replace('()', '')
    return not string
