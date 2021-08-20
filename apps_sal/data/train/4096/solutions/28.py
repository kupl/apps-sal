def valid_parentheses(string):
    string = ''.join([x for x in string if x in ['(', ')']])
    while '()' in string:
        string = string.replace('()', '')
    if len(string) != 0:
        return False
    return True
