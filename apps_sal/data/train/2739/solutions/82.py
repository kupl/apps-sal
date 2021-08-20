def cube_odd(arr):
    try:
        return sum(['x' if type(i) == bool else i ** 3 for i in arr if i ** 3 % 2 != 0])
    except:
        return None
