from operator import itemgetter
def first_n_smallest (arr, n):
    by_index, by_value = map(itemgetter, (0, 1))
    all_ascending = sorted(enumerate(arr), key=by_value)
    n_chronologic = sorted(all_ascending[:n], key=by_index)
    return list(map(by_value, n_chronologic))
