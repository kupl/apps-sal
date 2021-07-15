def valid_parentheses(string):
    new = ''.join([i for i in string if i in '()'])
    while '()' in new:
        new = new.replace('()', '')
    return len(new) == 0
