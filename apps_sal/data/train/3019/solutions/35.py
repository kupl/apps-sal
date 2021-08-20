def str_count(s, l):
    return len([i for i in range(len(s)) if s.startswith(l, i)])
