from itertools import chain


def merge_sort(words):
    if len(words) <= 1:
        return words
    midpt = len(words) // 2
    arr1 = merge_sort(words[:midpt])
    arr2 = merge_sort(words[midpt:])
    res = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] > arr2[0]:
            res.append(arr2.pop(0))
        else:
            res.append(arr1.pop(0))
    if len(arr1) > 0:
        res.extend(arr1)
    else:
        res.extend(arr2)
    return res


def sort(words):
    if not words:
        return []
    dict_by_alpha = dict()
    for a in alphabet:
        dict_by_alpha[a] = []
    for w in words:
        dict_by_alpha[w[0]] += [w]
    return chain.from_iterable((merge_sort(dict_by_alpha[a]) for a in alphabet))
