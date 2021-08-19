def count_sheep(n):
    i = 1
    string = ''
    while i <= n:
        string += '%d sheep...' % i
        i += 1
    return string
