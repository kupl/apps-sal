def pattern(n):
    output = []
    for i in range (1, n + 1):
        wing = ' ' * (n - i) + ''.join(str(d % 10) for d in range(1, i))
        output.append(wing + str(i % 10) + wing[::-1])
    return '\n'.join(output)
