from math import ceil

D = {"fire": "grass", "water": "fire", "grass": "water", "electric": "water"}


def calculate_damage(a, b, n, m):
    return ceil(50 * (n / m) * (2 if D[a] == b else 0.5 if D[b] == a or a == b else 1))
