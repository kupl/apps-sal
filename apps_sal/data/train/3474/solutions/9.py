def pattern(n):
    if n == 1:
        return '1'
    elif n > 1:
        return pattern(n - 1) + '\n1{}{}'.format('*' * (n - 1), n)
