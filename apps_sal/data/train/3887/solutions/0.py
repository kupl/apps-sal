def pattern(n):
    top = [(str(i % 10) * n).center(n * 3 - 2) for i in range(1, n)]
    left = ''.join(str(i % 10) for i in range(1, n))
    middle = left + str(n % 10) * n + left[::-1]
    return '\n'.join(top + [middle] * n + top[::-1])

