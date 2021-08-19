def braces_status(string):
    s = ''.join([b for b in string if b in '(){}[]'])
    while any((b in s for b in ['()', '{}', '[]'])):
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return True if len(s) == 0 else False
