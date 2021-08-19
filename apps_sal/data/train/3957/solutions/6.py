def uniq_c(seq):
    m = []
    (n, i) = (len(seq), 0)
    while i < n:
        c = seq[i]
        j = i + 1
        while j < n and seq[j] == c:
            j += 1
        m.append((c, j - i))
        i = j
    return m
