def duplicates(arr):
    return sum([arr.count(item) // 2 for item in set(arr)])
