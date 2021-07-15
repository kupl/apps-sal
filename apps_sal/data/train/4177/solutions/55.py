def men_from_boys(arr):
    return sorted([el for el in set(arr) if el % 2 == 0]) + sorted([el for el in set(arr) if el % 2 == 1], key=lambda el: -el)

