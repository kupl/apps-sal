def fat_fingers(string):
    if string is None:
        return None
    ret = []
    capslock = False
    for c in string:
        if c in 'aA':
            capslock = not capslock
        else:
            ret.append(c.swapcase() if capslock else c)
    return ''.join(ret)
