import math


def rat_at_layer_pos(layer, pos):
    if layer == pos == 0:
        return (1, 1)
    else:
        (a, b) = rat_at_layer_pos(layer - 1, pos // 2)
        return (a, a + b) if pos % 2 == 0 else (a + b, b)


def rat_at(n):
    layer = len(bin(n + 1)) - 3 if n > 0 else 0
    pos = n - int(2 ** layer - 1)
    print(layer, pos)
    return rat_at_layer_pos(layer, pos)


def index_layer_pos(a, b):
    if a == b == 1:
        return (0, 0)
    if a > b:
        (l, p) = index_layer_pos(a - b, b)
        return (l + 1, p * 2 + 1)
    else:
        (l, p) = index_layer_pos(a, b - a)
        return (l + 1, p * 2)


def index_of(a, b):
    (l, p) = index_layer_pos(a, b)
    return 2 ** l - 1 + p
