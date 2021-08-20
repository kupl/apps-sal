def capitalize(s, ind):
    sy = list(s)
    for i in ind:
        try:
            sy[i] = sy[i].upper()
        except IndexError:
            print('Index out of range')
    return ''.join(sy)
