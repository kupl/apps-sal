def cube_odd(arr):
    sum = 0
    for i in range(len(arr)):
        if type(arr[i]) != int:
            return None
        if arr[i] % 2 == 1:
            sum += arr[i] ** 3
    return sum
