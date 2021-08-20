def count_sheep(n):
    sheep_list = []
    sheep = '{} sheep...'
    while n >= 1:
        iteration = sheep.format(n + 1 - 1)
        sheep_list.append(iteration)
        n -= 1
    sheep_list.reverse()
    return ''.join(sheep_list)
