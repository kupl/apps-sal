def pattern(n):
    numbers = [i * str(i) for i in range(1, n + 1)]
    return '\n'.join(numbers)
