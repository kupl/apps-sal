def highest_rank(arr):
    return max(sorted(arr, reverse=True), key=arr.count)
