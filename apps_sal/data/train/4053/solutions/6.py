def reverse_factorial(num):
    s = 1
    i = 2
    while s != num:
        if s > num:
            return 'None'
        s *= i
        i += 1
    return str(i - 1) + '!'
