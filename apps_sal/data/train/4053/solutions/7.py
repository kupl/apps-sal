def reverse_factorial(num):
    c = 1
    while num % c == 0:
        num = num / c
        if num == 1:
            break
        c += 1
    else:
        return 'None'
    return '{}!'.format(c)
