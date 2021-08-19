from itertools import count


def center_of(s):
    if not s:
        return ''
    (seq, le, i) = ('', len(s), 0)
    for k in count(1):
        seq += s[i % le]
        i += 4 * k
        n = len(seq) / 3
        if n.is_integer():
            n = int(n)
            if seq[:n] == seq[n:n * 2] == seq[n * 2:] and i >= le:
                return seq[:n]
