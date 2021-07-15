def count_sheep(n):
    output = ''
    counter = 1
    while n > 0:
        output += f'{counter} sheep...'
        n -= 1
        counter += 1
    return output
