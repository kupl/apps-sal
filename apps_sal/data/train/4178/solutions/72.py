def min_sum(arr):
    s_arr = sorted(arr)
    return sum((a * b for (a, b) in zip(s_arr[:len(s_arr) // 2], s_arr[::-1])))
