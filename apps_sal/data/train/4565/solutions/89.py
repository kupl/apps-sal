def replace_dots(str):
    if len(str) == 0:
        return ''
    else:
        return str.replace('.', '-') if '.' in str else 'no dots'
