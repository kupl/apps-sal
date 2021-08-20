def pattern(n):
    output = ''
    for x in range(1, n + 1):
        for y in range(1, x + 1):
            output += str(x)
        output += '\n'
    output = output[:len(output) - 1]
    return output
