def highest_rank(arr):
    return sorted(arr, key=lambda x: (arr.count(x), x))[-1]
