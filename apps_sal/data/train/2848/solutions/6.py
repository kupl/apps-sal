from itertools import combinations_with_replacement as c
def find(a, k): return sum(1for i in range(1, len(a) + 1)for j in c(a, i)if sum(j) == k)
