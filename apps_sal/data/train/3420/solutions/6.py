def absolute_values_sum_minimization(a):
    return min([x for x in a], key=lambda x: sum([abs(i - x) for i in a]))
