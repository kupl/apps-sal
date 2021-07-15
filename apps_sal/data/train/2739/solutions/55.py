def cube_odd(arr):
    accumulator = 0
    for eachvalue in arr:
        if type(eachvalue) != type(1):
            return None
        else:
            if eachvalue % 2 != 0:
                x = eachvalue**3
                accumulator = accumulator + x
    return accumulator

