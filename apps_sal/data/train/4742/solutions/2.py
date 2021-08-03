def duplicates(arr):
    return sum((arr.count(n) // 2 for n in set(arr)))
