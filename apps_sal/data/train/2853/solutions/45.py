def solve(arr):
    arr1 = arr[::-1]
    arr2 = list(dict.fromkeys(arr1))
    return arr2[::-1]
