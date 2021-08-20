def prod_int_partII(n, s):
    res = []
    stack = [[n, 2, []]]
    while stack:
        (m, d, store) = stack.pop(0)
        for i in range(d, int(m ** 0.5) + 1):
            if m % i == 0:
                res.append(store + [i] + [m // i])
                stack.append([m // i, i, store + [i]])
    filtred_res = list(filter(lambda x: len(x) == s, res))
    if filtred_res:
        return [len(res), len(filtred_res), filtred_res] if len(filtred_res) > 1 else [len(res), len(filtred_res), filtred_res[0]]
    else:
        return [len(res), 0, []]
