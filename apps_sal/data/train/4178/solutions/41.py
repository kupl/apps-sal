def min_sum(arr):
    lst = []
    for i in range(len(arr) // 2):
        lst.append(sorted(arr)[-i - 1] * sorted(arr)[i])
    return sum(lst)
