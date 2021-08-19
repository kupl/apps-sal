def sum_pow_dig_seq(start, n, k):
    seen = [start]
    for i in range(k):
        r1 = sum(map(lambda x: x**n, map(int, str(seen[-1]))))
        if r1 in seen:  # Cycle detected.
            h = seen.index(r1)
            cyc_patt_arr = seen[h:]
            patt_len = len(seen) - h
            last_term = cyc_patt_arr[(k - i - 1) % patt_len]
            break
        seen.append(r1)

    return [h, cyc_patt_arr, patt_len, last_term]
