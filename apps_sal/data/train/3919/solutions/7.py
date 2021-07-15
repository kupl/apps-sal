def shuffled_array(a):
    a.remove(sum(a) / 2)
    return sorted(a)
