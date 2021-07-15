count_inversions=lambda arr:sum(sum(k>j for k in arr[:i]) for i,j in enumerate(arr))
