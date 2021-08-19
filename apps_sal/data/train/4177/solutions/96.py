def men_from_boys(arr):
    return sorted((v for v in set(arr) if v % 2 == 0)) + sorted((v for v in set(arr) if v % 2), reverse=True)
