import math


def how_many_pizzas(n):
    x = math.floor(n * n / 64)
    w = round(n * n % 64 / 8)
    return f'pizzas: {x}, slices: {w}'
