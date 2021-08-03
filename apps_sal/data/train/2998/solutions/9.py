def atomic_number(electrons):
    n = 1
    sa = []
    while electrons > 0:
        s = min(electrons, n ** 2 * 2)
        electrons -= s
        sa.append(s)
        n += 1
    return sa
