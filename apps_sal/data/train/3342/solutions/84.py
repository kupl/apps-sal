def pattern(n):
    pattern = list()
    for i in range(1, n + 1):
        pattern.append(str(i) * i)
    return '\n'.join(pattern) if n > 0 else ''
