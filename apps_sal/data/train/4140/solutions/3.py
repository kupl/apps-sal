import copy


def bubblesort_once(l):
    res = copy.copy(l)
    for i in range(len(res) - 1):
        if res[i] > res[i + 1]:
            res[i], res[i + 1] = res[i + 1], res[i]
    return res
