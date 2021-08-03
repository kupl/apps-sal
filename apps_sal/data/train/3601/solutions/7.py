def find_nb(m):
    try:
        vol = int(m)
    except TypeError:
        return -1

    partial_sum = 0
    i = 0
    while partial_sum < vol:
        i += 1
        partial_sum += i**3

    if vol == partial_sum:
        return i
    else:
        return -1
