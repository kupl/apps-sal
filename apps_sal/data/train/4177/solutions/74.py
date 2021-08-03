def men_from_boys(arr):
    odd = sorted([i for i in set(arr) if i % 2], reverse=True)
    even = sorted([i for i in set(arr) if not i % 2])
    return even + odd
