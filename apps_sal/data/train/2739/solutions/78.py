def cube_odd(arr):
    cubed = []
    for i in arr:
        if type(i) != int:
            return None
        else:
            cubed.append(i ** 3)
    new_arr = []
    for x in cubed:
        if x % 2 != 0:
            new_arr.append(x)

    return sum(new_arr)
