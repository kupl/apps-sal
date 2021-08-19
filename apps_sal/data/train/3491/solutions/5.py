def substring(strng):
    if not strng or len(strng) <= 2:
        return strng
    max_str = ''
    start_ind = 0
    next_ind = 0
    for (ind, letter) in enumerate(strng):
        if strng[start_ind] != letter:
            if start_ind == next_ind:
                next_ind = ind
            elif len(set(strng[start_ind:ind + 1])) > 2:
                (start_ind, next_ind) = (next_ind, ind)
                continue
        if ind - start_ind + 1 > len(max_str):
            max_str = strng[start_ind:ind + 1]
    return max_str
