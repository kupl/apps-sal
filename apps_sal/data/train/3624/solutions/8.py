def distribution_of_candy(arr):
    c = 0
    while len(set(arr)) != 1:
        x = [(i + 1 if i % 2 else i) // 2 for i in arr[-1:] + arr[:-1]]
        arr = [(i + 1 if i % 2 else i) - (i + 1 if i % 2 else i) // 2 for i in arr]
        arr = [i + j for (i, j) in zip(arr, x)]
        c += 1
    return [c, arr.pop()]
