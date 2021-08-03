def max_sum(arr, ranges):
    x = [sum([arr[i] for i in range(R[0], R[1] + 1)]) for R in ranges]
    return max(x)
