def count_sheep(n):
    count = 1
    str = ''
    while count <= n:
        str += f'{count} sheep...'
        count += 1
    return str
