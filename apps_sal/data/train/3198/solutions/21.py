def check_exam(arr1, arr2):
    score = sum((4 if a == arr1[i] else 0 if not a else -1 for (i, a) in enumerate(arr2)))
    return 0 if score < 0 else score
