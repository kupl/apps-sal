def sierpinski(n):
    if n == 0:
        return '*'
    lower = sierpinski(n - 1).splitlines()
    result = [s.center(2 * len(s) + 1) for s in lower]
    result += [s + ' ' + s for s in lower]
    return '\n'.join(result)
