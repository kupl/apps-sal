def max_sum(arr, ranges):
    return max([sum([arr[b] for b in range(i[0], i[1] + 1)]) for i in ranges])
