def array_equalization(a, k):
    sum = {}
    for (i, n) in enumerate(a):
        arr = sum.get(n)
        if not arr:
            sum[n] = [i]
        else:
            sum[n].append(i)
    print(list(sum.values()))
    times_arr = []
    for arr in list(sum.values()):
        i = 0
        pos = 0
        times = 0
        while 1:
            if i >= len(arr) or pos < arr[i]:
                pos += k
                times += 1
            elif pos == arr[i]:
                pos += 1
                i += 1
            else:
                i += 1
            if pos >= len(a):
                break
        times_arr.append(times)
    return min(times_arr)
