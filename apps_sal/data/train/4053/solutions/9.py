def reverse_factorial(num):
    if num == 1:
        return '1!'
    i = 0
    while num > 1:
        i += 1
        (num, n) = divmod(num, i)
        if n > 0:
            return 'None'
    return '{}!'.format(i)
