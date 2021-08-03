def interv(list1, list2):
    out_list = []
    for el1, el2 in zip(list1, list2):
        out_list.append(el1)
        out_list.append(el2)
    return out_list


def faro_cycles(deck_size):
    original = [x for x in range(deck_size)]
    new = interv(original[:deck_size // 2], original[deck_size // 2:])
    n = 1
    while original != new:
        new = interv(new[:deck_size // 2], new[deck_size // 2:])
        n += 1

    return n
