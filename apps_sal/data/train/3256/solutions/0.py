def sum_pow_dig_seq(num, exp, k):
    seq = []
    for step in range(k):
        seq.append(num)
        num = sum((int(dig) ** exp for dig in str(num)))
        if num in seq:
            cycle_start = seq.index(num)
            cycle = seq[cycle_start:]
            last_term = cycle[(k - cycle_start) % len(cycle)]
            return [cycle_start, cycle, len(cycle), last_term]
    return [0, [], 0, num]
