def check_exam(arr1, arr2):
    return max(0, sum([4 if x == y else -1 if y else 0 for x, y in zip(arr1, arr2)]))
