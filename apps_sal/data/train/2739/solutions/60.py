def cube_odd(arr):
    output = 0
    for i in arr:
        if type(i) == int:
            if i % 2 != 0:
                output += i**3
        else:
            return None
    return output
