def powers(n):
    next_small = n.bit_length()
    total, lst = 0, []
    while next_small > -1:
        v = 1 << next_small
        if total + v <= n:
            total += v
            lst.append(v)
        if total == n:
            break
        next_small -= 1
    return lst[::-1]
