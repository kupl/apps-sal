def sum_pow_dig_seq(start, n, k):
    seq = [start]
    num = start
    for i in range(k):
        num = sum([int(x) ** n for x in str(num)])
        if num in seq:
            loop_starts_from = seq.index(num)
            loop_array = seq[loop_starts_from:]
            tail_size = loop_starts_from
            loop_size = len(loop_array)
            last_term = loop_array[(k - tail_size) % loop_size]
            return [tail_size, loop_array, loop_size, last_term]
        seq.append(num)
    else:
        return [len(seq), [], 0, seq[-1]]
