
def find(seq):
    seq.sort()
    first, last = seq[0], seq[-1]
    d = min(seq[1] - first, seq[2] - seq[1])
    n = (last - first) * 1.0 / d + 1
    s = n / 2 * (first + last)
    s_ = sum(seq)
    return s - s_
