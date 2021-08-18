def ulam_sequence(u, v, n):
    lst, seq, ex, q = [], 1, 1, 1 << v | 1 << u
    for _ in range(n):
        w = q & -q
        l = w.bit_length() - 1
        s = seq << l
        seq |= w
        lst.append(l)
        ex |= s & q
        q |= s
        q &= ~ex
    return lst
