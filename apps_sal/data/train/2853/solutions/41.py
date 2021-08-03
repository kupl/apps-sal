def solve(arr):
    x = list(set(arr))
    res = []
    indices = []
    result = []
    for num in x:
        index = last_index(arr, num)
        indices.append(index)
        res.append(arr[index])
    while len(indices) > 0:
        loc = indices.index(min(indices))
        result.append(res[loc])
        indices.pop(loc)
        res.pop(loc)
    return result


def last_index(pepe, n):
    return [i for i in range(len(pepe)) if pepe[i] == n][::-1][0]
