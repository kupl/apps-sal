def check_exam(arr1, arr2):
    return max(0, sum((arr1[i] == arr2[i]) * 5 - 1 for i in range(len(arr1)) if arr2[i]))
