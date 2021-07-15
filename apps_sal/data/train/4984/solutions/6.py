def meeting(s):
    return ''.join(sorted(('({1}, {0})'.format(*pair.split(':')) for pair in s.upper().split(';'))))
