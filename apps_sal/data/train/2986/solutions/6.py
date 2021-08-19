def segments(m, a):
    new_list = []
    for sub_list in a:
        new_list = new_list + list(range(sub_list[0], sub_list[1] + 1))
    new_set = set(new_list)
    expected_set = set(range(0, m + 1))
    return sorted(list(expected_set.difference(new_set)))
