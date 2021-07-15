def largest_sum(a):
    m = c = 0
    for i in a:
        c = max(0,c+i)
        m = max(m,c)
    return m
