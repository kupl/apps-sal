def sierpinski(n):
    if n == 0:
        return '*'
    lines = sierpinski(n - 1).split('\n')
    upper = [' ' * 2 ** (n - 1) + l + ' ' * 2 ** (n - 1) for l in lines]
    lower = [l + ' ' + l for l in lines]
    return '\n'.join(upper + lower)
