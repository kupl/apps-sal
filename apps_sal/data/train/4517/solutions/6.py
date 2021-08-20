def odd_one_out(s):
    k = {}
    out = []
    for x in s:
        k[x] = k.get(x, 0) + 1
    odd_list = [x for x in s if k[x] % 2 == 1]
    for x in odd_list:
        if k[x] == 1:
            out.append(x)
        else:
            k[x] = k.get(x) - 1
    return out
