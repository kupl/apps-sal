def find(seq):
    if len(seq) <= 1:
        return seq
    seq.sort()
    x = []
    t = 0
    for i in range(len(seq) - 1):
        if i == 0:
            t = seq[i + 1] - seq[i]
            x.append(t)
        else:
            t = seq[i + 1] - seq[i]
            if t != x[-1]:
                x.append(t)
                break
            else:
                x.append(t)
    return min(seq) + len(x) * x[0]
