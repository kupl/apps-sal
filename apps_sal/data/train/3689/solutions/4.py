def how_many_pizzas(n):
    pizzas = n * n / 64
    p = int(pizzas)
    s = int((pizzas - p) * 8)
    return f'pizzas: {p}, slices: {s}'
