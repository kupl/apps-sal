def men_from_boys(arr):
    arr = set(arr)
    return [i for i in sorted(arr) if i % 2 == 0] + [i for i in sorted(arr, reverse=True) if i % 2]
