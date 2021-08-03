def base_finder(seq):
    str = ''
    for i in seq:
        str += i

    return len(set(str))
