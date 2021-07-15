def shuffled_array(s):
    s.remove(sum(s)//2)
    s.sort()
    return s
