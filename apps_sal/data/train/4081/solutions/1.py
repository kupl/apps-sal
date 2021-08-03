def first_tooth(array):
    array = [array[0]] + array + [array[-1]]
    diffs = [2 * array[i] - array[i - 1] - array[i + 1] for i in range(1, len(array) - 1)]
    m = max(diffs)
    if diffs.count(m) > 1:
        return -1
    else:
        return diffs.index(m)
