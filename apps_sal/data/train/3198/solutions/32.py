def check_exam(arr1, arr2):
    return max(sum((4 if arr1[i] == arr2[i] else -1 if arr2[i] else 0 for i in range(len(arr1)))), 0)
