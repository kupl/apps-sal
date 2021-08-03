def check_exam(arr1, arr2):
    return max(sum((-1, 4)[a == b] for a, b in zip(arr1, arr2) if b), 0)
