def array(string):
    s = string.replace(' ', '').split(',')
    return ' '.join(s[1:-1]) if s[1:-1] != [] else None
