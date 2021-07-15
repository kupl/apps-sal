def max_tri_sum(arr):
    return sum(sorted(set(arr))[-3:])
