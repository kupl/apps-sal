def reverse_fun(arr):
    for i in range(len(arr)):
        arr = arr[0:i] + arr[i:][::-1]
    return arr
