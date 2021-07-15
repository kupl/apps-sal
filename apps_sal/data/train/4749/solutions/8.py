def base_finder(seq):
    return max([int(i) for i in "".join(seq)]) + 1
