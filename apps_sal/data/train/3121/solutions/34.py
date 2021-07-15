def solve(arr):
    duplicates = [x for x in arr if arr.count(x) > 1]
    return duplicates[0] if duplicates else sum(arr)
