def is_madhav_array(arr):
    nTerms = ((1 + 8 * len(arr)) ** 0.5 - 1) / 2
    return len(arr) > 1 and (not nTerms % 1) and (len({sum(arr[int(i * (i + 1) // 2):int(i * (i + 1) // 2) + i + 1]) for i in range(int(nTerms))}) == 1)
