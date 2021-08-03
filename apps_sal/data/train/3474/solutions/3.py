def pattern(n):
    if n == 1:
        return "1"
    else:
        return '1\n' + ''.join([str(1) + '*' * (i - 1) + str(i) + '\n' for i in range(2, n + 1)])[:-1]
