def min_sum(arr):
    arr.sort()
    return sum(arr[x]*arr[-x-1] for x in range(int(len(arr)/2)))


