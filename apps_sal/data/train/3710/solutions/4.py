def ulam_sequence(u0, u1, n):
    sequence = [u0, u1]
    good = {u0+u1}
    bad = set()
    while len(sequence) < n:
        k = min(good)
        good.remove(k)
        for h in sequence:
            s = k + h
            if s in good:
                good.remove(s)
                bad.add(s)
            elif s not in bad:
                good.add(s)
        sequence.append(k)
    return sequence

