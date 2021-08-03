def sum_of_digits_pow(n, e):
    return sum([i**e for i in map(int, str(n))])


def sum_pow_dig_seq(start, e, k):
    h = 0
    cyc_patt_arr, sums = [], []
    for i in range(1, k + 1):
        start = sum_of_digits_pow(start, e)
        if not cyc_patt_arr and start in sums:
            cyc_patt_arr = [j for j in sums[sums.index(start):]]
            h = sums.index(start) + 1
            return [h, cyc_patt_arr, len(cyc_patt_arr), cyc_patt_arr[(k - i) % len(cyc_patt_arr)]]
        sums.append(start)
