def check_exam(arr1, arr2):
    return max(0, sum([4 if arr1[i] == arr2[i] else 0 if arr2[i] == '' else -1 for i in range(len(arr1))]))
