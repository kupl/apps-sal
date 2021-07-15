def cube_odd(arr):
    for item in arr:
        if type(item) != int:
            return

    return sum(i**3 for i in arr if i % 2 != 0)
