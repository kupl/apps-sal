def shuffled_array(a):
    return a.remove(sum(a) / 2) or sorted(a)
