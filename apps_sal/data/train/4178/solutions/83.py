def min_sum(arr):
    arr = sorted(arr)
    output = 0
    for i in range(0,len(arr)//2):
        output += arr[i] * arr[(-(i+1))]
    return output
