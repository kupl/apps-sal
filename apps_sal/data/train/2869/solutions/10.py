def distinct(seq):
    s = set(seq)
    return [s.remove(n) or n for n in seq if n in s]
