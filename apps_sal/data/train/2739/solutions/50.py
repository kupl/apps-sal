def cube_odd(arr):
    new_arr = []
    for i in range(len(arr)):
        if type(arr[i]) == bool:
            return None
        if type(arr[i]) == str:
            return None
        new_arr.append(arr[i] ** 3)
    value = 0
    for i in range(len(new_arr)):
        if new_arr[i] % 2 == 1:
            value += new_arr[i]
    return value

