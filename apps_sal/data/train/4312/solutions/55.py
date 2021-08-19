from itertools import groupby


def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    if not arr:
        return result
    arr = dict(enum((list(j) for (i, j) in groupby(arr))))
    keys = sorted(arr.keys())
    for i in arr:
        if i != keys[0] and i != keys[-1]:
            curr = arr[i][0]
            prev = arr[keys[keys.index(i) + 1]][0]
            post = arr[keys[keys.index(i) - 1]][0]
            if curr > post and curr > prev:
                result['pos'] = result['pos'] + [i]
                result['peaks'] = result['peaks'] + [arr[i][0]]
    return result


def enum(listA):
    value = 0
    for j in listA:
        if len(j) == 1:
            yield (value, j)
            value += 1
        else:
            yield (value, j)
            value += len(j)
