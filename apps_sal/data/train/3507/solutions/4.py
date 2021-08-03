from collections import defaultdict


def delete_nth(order, max_e):
    dct = defaultdict(int)
    res = []
    for i in order:
        dct[i] += 1
        if dct[i] <= max_e:
            res.append(i)
    return res
