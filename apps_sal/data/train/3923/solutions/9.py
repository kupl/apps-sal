def micro_world(arr, k):
    x = arr.copy()
    for i in arr:
        for j in range(i - k, i):
            while j in x:
                x.remove(j)
    return len(x)
