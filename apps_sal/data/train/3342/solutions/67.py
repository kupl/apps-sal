def pattern(n):
    if n <= 0:
        return ''
    elif n == 1:
        return '1'
    else:
        ls = ['1']
        for i in range(2, n + 1):
            ls.append('\n' + f'{i}' * i)
        return ''.join(ls)
