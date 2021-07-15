def count_sheep(n):
    return ''.join(f'{x+1} sheep...' for x in range(n))
