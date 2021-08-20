def get_combos(arr, comm):
    if len(arr) == 1:
        return [arr]
    comm = comm.replace(' ', '')
    sublists = get_combos(arr[:-1], comm)
    newlists = []
    for sublist in sublists:
        if comm == '>>' and arr[-1] < sublist[-1] or (comm == '<<' and arr[-1] > sublist[-1]):
            newlists.append(sublist + [arr[-1]])
        newlists.append(sublist)
    newlists.append([arr[-1]])
    return newlists


def longest_comb(arr, comm):
    combos = get_combos(arr, comm)
    max_length = 3
    longest_combos = []
    for combo in combos:
        if len(combo) == max_length:
            longest_combos.append(combo)
        elif len(combo) > max_length:
            max_length = len(combo)
            longest_combos = [combo]
    if len(longest_combos) == 1:
        return longest_combos[0]
    else:
        return longest_combos
