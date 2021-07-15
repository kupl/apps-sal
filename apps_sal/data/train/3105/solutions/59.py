def count_sheep(n):
    return ' sheep...'.join(list(str(x+1) for x in range(n))) + ' sheep...'
