def repeats(arr):
    single = []
    for i in arr:
        if arr.count(i) == 1:
            single.append(i)
    total = sum(single)
    return total
