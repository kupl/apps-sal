def pattern(n):
    solution = ''
    if n < 1:
        return solution
    for i in range(1, n + 1):
        solution += f'{i}' * i
        solution += '\n'
    return solution[:-1]
