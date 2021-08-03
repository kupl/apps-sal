def sum_arrays(arrays, shift):
    l = []
    for i in range(len(arrays)):
        tmp = i * shift * [0] + arrays[i] + (len(arrays) - i - 1) * shift * [0]
        l.append(tmp)
    res = []
    for i in range(len(l[0])):
        tmp = sum([ii[i] for ii in l])
        res.append(tmp)
    return res
