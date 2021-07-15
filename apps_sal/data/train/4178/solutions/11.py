def min_sum(arr):
    sum = 0
    reduced_arr = arr
    iters = int(len(arr)/2)
    for i in range(iters):
        sum += min(reduced_arr) * max(reduced_arr)
        reduced_arr.remove(min(reduced_arr))
        reduced_arr.remove(max(reduced_arr))
    return sum
