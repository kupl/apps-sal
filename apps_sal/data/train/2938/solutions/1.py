def pattern(n):
    result = []
    for i in range(1, n + 1):
        string = ''
        for j in range(n, i, -1):
            string += ' '
        for j in range(1, i):
            string += str(j)[-1]
        for j in range(i, 0, -1):
            string += str(j)[-1]
        for j in range(n, i, -1):
            string += ' '
        result.append(string)
    return '\n'.join(result)
