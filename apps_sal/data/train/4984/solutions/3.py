def meeting(s):
    names = s.upper().split(';')
    return ''.join(sorted(('({1}, {0})'.format(*n.split(':')) for n in names)))
