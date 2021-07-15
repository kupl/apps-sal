def pattern(n):
    if n < 1:
        return ''
    elif n == 1:
        return str(1)
    else:
        return pattern(n-1) + '\n' + str(n) * n
