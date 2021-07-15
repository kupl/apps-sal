def remove(s):
    return '{}{}'.format(s.replace('!', ''), '!' * (len(s) - len(s.rstrip('!'))))
