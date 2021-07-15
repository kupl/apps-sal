def min_sum(arr):
    arr_sorted = sorted(arr)
    cut = int(len(arr_sorted)/2)
    pairs = list(zip(arr_sorted[:cut], arr_sorted[cut:][::-1]))
    return sum(a*b for a,b in pairs)
