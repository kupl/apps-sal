def check_exam(arr1, arr2):
    a = sum([4 if arr1[x] == arr2[x] else -1 if arr2[x] is not '' else 0 for x in range(len(arr1))])
    return a if a >= 0 else 0
