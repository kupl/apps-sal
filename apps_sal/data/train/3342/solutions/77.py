def pattern(n):
    pattern = ''
    for i in range(1, n + 1):
        for x in range(1, i + 1):
            pattern += str(i)
        if i + 1 != n + 1:
            pattern += str('\n')
    return pattern
