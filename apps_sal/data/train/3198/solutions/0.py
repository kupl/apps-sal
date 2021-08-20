def check_exam(arr1, arr2):
    return max(0, sum((4 if a == b else -1 for (a, b) in zip(arr1, arr2) if b)))
