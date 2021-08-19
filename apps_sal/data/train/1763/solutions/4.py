def insane_inc_or_dec(Q):
    return (reduce(lambda D, V: D * (1 + V + Q), range(9), 1) * (20 + Q) / 3628800 - 10 * Q - 2) % 12345787
