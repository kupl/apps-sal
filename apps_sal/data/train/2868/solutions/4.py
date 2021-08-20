def is_nice(l):
    return l != [] and [e for e in l if e - 1 not in l and e + 1 not in l] == []
