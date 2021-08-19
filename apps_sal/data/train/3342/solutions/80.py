def pattern(n):
    output = ''
    for i in range(1, n + 1):
        for j in range(i):
            output += str(i)
        if i < n:
            output += '\n'
    return output
