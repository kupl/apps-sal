def duplicates(arr):
    return sum((arr.count(i) // 2 for i in set(arr)))
