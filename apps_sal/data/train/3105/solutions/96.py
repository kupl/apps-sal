def count_sheep(n):
    result = ''
    x = 1
    while x <= n:
        result = result + str(x) + ' sheep...'
        x = x + 1
    return result


count_sheep(3)
