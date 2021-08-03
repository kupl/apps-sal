def hungry_seven(arr):
    for i in range(len(arr) - 2):
        if arr[i] == 7 and arr[i + 1] == 8 and arr[i + 2] == 9:
            return hungry_seven(arr[:i] + arr[i + 1:i + 3] + [7] + arr[i + 3:])
    return arr
