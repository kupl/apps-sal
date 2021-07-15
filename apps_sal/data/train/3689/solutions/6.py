def how_many_pizzas(n):
    return 'pizzas: {}, slices: {}'.format(n ** 2 // 8 ** 2, n ** 2 % 8 ** 2 // 8)
