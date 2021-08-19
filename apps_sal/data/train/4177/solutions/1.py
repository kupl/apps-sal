def men_from_boys(arr):
    return sorted(set(arr), key=lambda n: (n % 2, n * (-1) ** (n % 2)))
