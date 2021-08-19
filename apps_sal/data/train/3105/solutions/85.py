def count_sheep(n):
    counter = ''
    for i in range(1, n + 1):
        counter += str(i) + ' sheep...'
    return counter
