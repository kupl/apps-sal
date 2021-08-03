def solve(arr):
    return sorted(arr, key=lambda x: (-arr.count(x), x))
