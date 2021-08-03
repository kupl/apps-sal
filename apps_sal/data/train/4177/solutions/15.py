def men_from_boys(arr):
    return sorted(set(arr), key=lambda i: ~(4**5 + i) * (i % 2) or -5**5 + i)
