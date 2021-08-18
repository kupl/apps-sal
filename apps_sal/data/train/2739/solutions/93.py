def cube_odd(arr):
    try:
        sum = 0
        for i in range(len(arr)):
            if i >= len(arr):
                break
            else:
                a = (i)
                if str(arr[a]) in ["True", "False"]:
                    return None
                elif arr[a] % 2 == 1:
                    sum += (arr[a]**3)
        return sum
    except TypeError:
        return None
