def men_from_boys(arr):
    arr = sorted(set(arr))
    return [i for i in arr if i%2 == 0] + [i for i in arr[::-1] if i%2]
