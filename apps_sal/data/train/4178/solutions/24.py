def min_sum(arr):
    sum_list = []
    arr = sorted(arr)
    for i in range(len(arr) // 2):
        sum_list.append(arr[i] * arr[-(i + 1)])
    return sum(sum_list)
