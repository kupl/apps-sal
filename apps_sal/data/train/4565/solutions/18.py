def replace_dots(s):
    if s == '':
        return ''
    elif '.' not in s:
        return 'no dots'
    else:
        return s.replace('.', '-')
