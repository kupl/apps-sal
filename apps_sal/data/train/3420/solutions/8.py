from bisect import *
def absolute_values_sum_minimization(A):
    return min(A,key=lambda r:(sum(abs(v-r)for v in A)))
