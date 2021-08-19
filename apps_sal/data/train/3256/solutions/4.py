def sum_pow_dig_seq(start, n, k):

    def next_(v):
        return sum((int(c) ** n for c in str(v)))
    history = []
    history_set = set()
    x = start
    while True:
        if x in history_set:
            i = history.index(x)
            cyc = history[i:]
            if k < len(history):
                return [i, cyc, len(cyc), history[k]]
            return [i, cyc, len(cyc), cyc[(k - i) % len(cyc)]]
        history.append(x)
        history_set.add(x)
        x = next_(x)
