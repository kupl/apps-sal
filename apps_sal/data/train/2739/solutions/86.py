def cube_odd(arr):
    sum = 0
    for i in arr:
        if type(i) in (int,):
            if i % 2:
                sum += i ** 3
        else:
            return None
    return sum
