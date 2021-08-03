def rgb(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))
