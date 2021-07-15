def absolute_values_sum_minimization(A):
    lst = [[sum([abs(j-i) for j in A]), i] for i in A]
    return sorted(lst)[0][-1]
