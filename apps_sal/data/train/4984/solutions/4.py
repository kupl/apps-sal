def meeting(s):
    return ''.join(sorted(('(%s, %s)' % tuple(e.split(':')[::-1]) for e in s.upper().split(';'))))
