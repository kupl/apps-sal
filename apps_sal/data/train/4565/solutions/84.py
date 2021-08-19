def replace_dots(str):
    import re
    if str == '':
        return str
    return re.sub('\\.', '-', str) if str.count('.') else 'no dots'
