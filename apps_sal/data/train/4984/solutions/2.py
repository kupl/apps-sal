def meeting(s):
    return ''.join((f'({a}, {b})' for (a, b) in sorted((name.split(':')[::-1] for name in s.upper().split(';')))))
