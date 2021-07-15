def min_sum(arr):
    arr = sorted(arr)
    lst = [arr[i] * arr[-(i+1)] for i in range(int(len(arr)/2))]
    return sum(lst)
