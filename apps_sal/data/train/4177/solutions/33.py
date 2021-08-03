def men_from_boys(arr):
    even = sorted(filter(lambda x: x % 2 == 0, set(arr)))
    odd = sorted(filter(lambda x: x % 2 == 1, set(arr)), reverse=True)
    even.extend(odd)
    return even
