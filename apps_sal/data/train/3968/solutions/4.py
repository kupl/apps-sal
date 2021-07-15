def tail_swap(lst):
    (a,b),(c,d) = (s.split(':') for s in lst)
    return list(map(':'.join, ((a,d),(c,b))))
