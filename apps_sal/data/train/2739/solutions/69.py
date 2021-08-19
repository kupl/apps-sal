def cube_odd(arr):
    sum = 0
    for x in arr:
        if type(x) == int:
            if x % 2 == 1:
                sum += x ** 3
        else:
            return None
    return sum
