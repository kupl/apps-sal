def valid_parentheses(string):
    string = ''.join([x for x in string if x in '()'])
    try:
        string = string.replace('()', '')
        return valid_parentheses(string) if string else True
    except:
        return False
