def pattern(n):
    return '\n'.join(''.join(str(j % 10) for j in range(n, i, -1)) + str(i % 10) * i for i in range(n, 0, -1))
