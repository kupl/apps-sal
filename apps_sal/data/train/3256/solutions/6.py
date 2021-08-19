def sum_pow_dig_seq(start, n, k):
    x = start
    series = []
    seen_at = {}
    i = 0
    while x not in seen_at:
        series.append(x)
        seen_at[x] = i
        x = sum((int(d) ** n for d in str(x)))
        i += 1
    i_first = seen_at[x]
    cycle_length = i - i_first
    if k >= i:
        k = i_first + (k - i_first) % cycle_length
    return [i_first, series[i_first:], cycle_length, series[k]]
