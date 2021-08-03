def rank_of_element(a, i): return sum(n < a[i] + (j < i)for j, n in enumerate(a))
