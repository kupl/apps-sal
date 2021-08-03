def check_exam(arr1, arr2):
    a = sum(4 if x == y else -1 if y else 0 for x, y in zip(arr1, arr2))
    return a if a > 0 else 0
