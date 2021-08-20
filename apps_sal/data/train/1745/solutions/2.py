def calculate(s):
    if any((c not in '.0123456789+-*$' for c in s)):
        return '400: Bad request'
    tokens = [float(e) if e not in '$*-+' else e for e in s.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('$', ' $ ').split()]
    for c in '$*-+':
        r = []
        for t in tokens:
            if r and r[-1] == c:
                r.pop()
                t = {'$': lambda a, b: a / b, '*': lambda a, b: a * b, '-': lambda a, b: a - b, '+': lambda a, b: a + b}[c](r.pop(), t)
            r.append(t)
        tokens = r
    return tokens.pop()
