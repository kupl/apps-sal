def rad_ladies(name):
    return ''.join((i.upper() for i in name if i.isalpha() or i == ' ' or i == '!'))
