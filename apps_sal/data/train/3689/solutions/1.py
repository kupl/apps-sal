def how_many_pizzas(n):
    pizzas, slices = (int(n) for n in divmod(n**2, 64))
    return f"pizzas: {pizzas}, slices: {slices // 8}"
