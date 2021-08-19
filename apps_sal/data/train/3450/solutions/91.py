def array(s):
    s = s.replace(' ', '').replace(',', ' ').split(' ')
    return ' '.join(s[1:len(s) - 1]) if len(s) > 2 else None
