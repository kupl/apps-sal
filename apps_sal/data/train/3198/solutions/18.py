def check_exam(arr1,arr2):
    return max(sum([0 if arr2[i] == '' else 4 if arr1[i] == arr2[i] else -1 for i in range(0, len(arr1))]), 0)
