def pattern(n):
    if n < 1:
        return ''
    elif n == 1:
        return '1'
    return '\n'.join([x * f'{x}' for x in range(1, n + 1)])
