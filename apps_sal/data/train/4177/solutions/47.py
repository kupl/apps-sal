def men_from_boys(arr):
    a, b = filter(lambda x: x % 2 == 0, arr), filter(lambda x: x % 2 == 1, arr)
    return sorted(list(set(a))) + sorted(list(set(b)), reverse=True)
