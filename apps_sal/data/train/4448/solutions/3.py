def get_derivative(s):
    if 'x' not in s:
        return '0'
    elif s[-1] == 'x':
        return s[:-1]
    else:
        (b, e) = [int(p) for p in s.split('x^')]
        return f"{b * e}x{('^' + str(e - 1) if e != 2 else '')}"
