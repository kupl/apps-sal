def men_from_boys(arr):
    arr = set(arr)
    even = sorted([i for i in arr if not i % 2])
    even.extend(sorted([i for i in arr if i % 2], reverse=True))
    return even
