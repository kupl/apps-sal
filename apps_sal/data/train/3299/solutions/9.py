def calc(a):
    res = [0] * (len(a) + 1)
    for k in range(1, len(a) + 1):
        new_res = []
        new_res_size = len(res) - 1
        for i in range(new_res_size):
            j = i + k
            new_res.append(2 * max(a[i] + res[i + 1], a[j - 1] + res[i]))
        res = new_res
    return res[0]
