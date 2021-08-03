def cube_odd(arr):
    arr1 = []
    result = 0
    try:
        for i in arr:
            if type(i) == bool:
                return None
            else:
                if i % 2 != 0:
                    result = i**3
                    arr1.append(result)
        return sum(arr1)
    except TypeError:
        return None
