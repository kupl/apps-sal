def cube_odd(arr):
    result = 0
    for el in arr:
        if type(el) != int:
            return None
        if el % 2 != 0:
            result += el*el*el
    return result 
