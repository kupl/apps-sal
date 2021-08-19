def pattern(n):
    return '\n'.join((i * str(i) for i in range(n + 1))).lstrip()
