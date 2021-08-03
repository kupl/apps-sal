def double_char(s):
    return ''.join(['{}'.format(i[0] + i[1]) for i in zip(s, s)])
