def how_many_pizzas(n):
    q, r = divmod(n**2, 8**2)
    return f"pizzas: {q}, slices: {round(r / 8)}"
