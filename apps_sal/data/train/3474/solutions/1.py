def pattern(n):
    s = ''
    for i in range(n):
        if i == 0:
            s += '1\n'
        else:
            s += '1{}{}\n'.format('*' * i, i + 1)
    return s.rstrip('\n')
