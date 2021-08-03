def find_average(arr):
    x = len(arr)
    sum = 0

    for i in range(x):
        sum = sum + arr[i]

    return sum / x
