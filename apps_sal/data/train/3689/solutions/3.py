def how_many_pizzas(n):
    return f'pizzas: {n * n // 8 ** 2}, slices: {n * n / 8 % 8:.0f}'
