def check_exam(arr1, arr2):
    return max(0, sum([4 if arr2[i] == x else 0 if arr2[i] == '' else -1 for (i, x) in enumerate(arr1)]))
