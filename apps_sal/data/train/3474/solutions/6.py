def pattern(n):
    return '\n'.join(('1{}{}'.format('*' * i, '' if i == 0 else i + 1) for i in range(n)))
