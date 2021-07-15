def pattern(n):
    return '\n'.join([str(index + 1) * (index + 1) for index in range(n)])
