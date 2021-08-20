def how_many_pizzas(n):
    area = n * n
    eight_area = 64
    total_pizzas = int(area / eight_area)
    slices = 0
    if area % eight_area != 0:
        slices = int((area - total_pizzas * eight_area) / 8)
    return 'pizzas: {}, slices: {}'.format(total_pizzas, slices)
