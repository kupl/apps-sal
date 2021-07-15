def int_diff(arr, n):
    return sum([len([(i, j) for j in range(i+1, len(arr)) if abs(arr[i]-arr[j])==n]) for i in range(len(arr))])
