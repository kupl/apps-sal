def count_inversions(arr): return sum(sum(k > j for k in arr[:i]) for i, j in enumerate(arr))
