def men_from_boys(arr):
    return sorted(set(arr), key=lambda x: (x%2 != 0, 0-x if x%2 else x))
