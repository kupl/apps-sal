def reorder(a, b):
    arr1, arr2 = list(range(a // 2)), list(range(a // 2, a))
    for _ in range(b): arr1, arr2 = [arr1[-1]] + arr1[:-1], [arr2[-1]] + arr2[:-1]
    return [arr1, arr2]
