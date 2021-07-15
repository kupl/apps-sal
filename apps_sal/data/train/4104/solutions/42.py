from heapq import nlargest

max_tri_sum = lambda lst: sum(nlargest(3, set(lst)))
