def rad_ladies(name):
    return ''.join((i.upper() for i in name if not i.isdigit() and i not in '%$&/£?@'))
