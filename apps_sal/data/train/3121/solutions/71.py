def solve(arr):
    return sum(arr) / arr.count(max(arr, key=arr.count))
