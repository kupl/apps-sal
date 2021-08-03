def pattern(n):
    return '\n'.join([str(num) * num for num in range(1, n + 1, 2)])
