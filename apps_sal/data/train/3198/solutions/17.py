def check_exam(arr1, arr2):
    ans = sum([4 if ca == sa else 0 if sa == '' else -1 for (ca, sa) in zip(arr1, arr2)])
    return ans if ans > 0 else 0
