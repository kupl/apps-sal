def men_from_boys(arr):
    return sorted(set(arr), key=lambda a: (a % 2, [a, -a][a % 2]))

