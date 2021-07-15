def total(arr):
    fin_arr = []
    for i in range(2, len(arr)):
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            fin_arr.append(arr[i])
    n = sum(fin_arr)
    return n
