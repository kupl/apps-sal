def solve(arr):
    unique = set(arr)
    for num in unique:
        for i in range(arr.count(num) - 1):
            arr.pop(arr.index(num))
    return arr
