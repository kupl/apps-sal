def how_many_pizzas(n):
    return 'pizzas: {}, slices: {}'.format(*divmod(n * n // 8, 8))
