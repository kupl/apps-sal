absolute_values_sum_minimization=lambda li:min([[sum([abs(j-k)for k in li]),j]for i,j in enumerate(li)])[1]
