def cube_odd(arr):
    if arr == [x for x in arr if type(x) == int]: return sum([i**3 for i in arr if i % 2 == 1])

