def valid_parentheses(string):
    string = ''.join(i for i in string if i == '(' or i == ')')
    while '()' in string:
        string = string.replace('()', '')
    return string == ''
