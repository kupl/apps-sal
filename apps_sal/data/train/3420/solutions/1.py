def absolute_values_sum_minimization(A):
    d = {x: sum(abs(n-x) for n in A) for x in A}
    return min(d, key=lambda x: (d[x], x))
