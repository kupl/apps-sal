def cube_odd(arr):
    sum = 0
    for i in range(len(arr)):
        if type(arr[i]) != int:
            return None
        elif arr[i] % 2 != 0:
            sum += arr[i] ** 3
    return sum
