def cube_odd(arr):
    total = 0
    for elem in arr:
        if type(elem) == int:
            if elem % 2 == 1:
                total += elem**3
        else:
            return None
    return total
