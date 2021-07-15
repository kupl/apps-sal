def ulam_sequence(u0, u1, n):
    seq = [u0, u1]
    for _ in range(n - 2):
        sums = sorted([seq[i] + seq[j] for i in range(len(seq)) for j in range(i, len(seq)) if i != j])
        seq.append(next(s for s in sums if sums.count(s) == 1 and s not in seq))
    return seq
