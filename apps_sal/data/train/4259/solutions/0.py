def pattern(n, *x):
    if n < 1:
        return ''
    x = x[0] if x and x[0] > 0 else 1
    result = []
    for i in range(1, n + 1):
        line = ' ' * (i - 1) + str(i % 10) + ' ' * (n - i)
        result.append(line + line[::-1][1:] + (line[1:] + line[::-1][1:]) * (x - 1))
    return '\n'.join(result + result[::-1][1:])
