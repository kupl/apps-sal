from re import findall

def dashatize(num):
    return '-'.join(findall('([13579]|[02468]+)', str(num))) or 'None'
