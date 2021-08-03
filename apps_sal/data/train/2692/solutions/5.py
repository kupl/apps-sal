def swap(l, aindex, bindex):
    tmp = l[bindex]
    l[bindex] = l[aindex]
    l[aindex] = tmp


def bubble(l):
    result = []
    for _ in range(len(l) - 1):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                swap(l, i, i + 1)
                result.append(list(l))
    return result
