def F(n):
    return sum(int(d)**2 for d in str(n))

def repeat_sequence_len(n):
    seq = [n]
    c = F(n)
    while c not in seq:
        seq.append(c)
        c = F(c)
    return len(seq) - seq.index(c)
