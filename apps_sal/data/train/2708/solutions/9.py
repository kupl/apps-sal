def yes_no(arr):
    r = []
    for i in range(0, len(arr) * 2 - 1, 2):
        r.append(arr[i])  # using only append because it is o(1), while remove is o(n)
        if i < len(arr) - 1:
            arr.append(arr[i + 1])
    return r
