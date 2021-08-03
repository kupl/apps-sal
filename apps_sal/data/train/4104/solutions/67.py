def max_tri_sum(a):
    a.sort()
    q = []
    [q.append(i) for i in a if i not in q]
    return sum(q[-3:])
