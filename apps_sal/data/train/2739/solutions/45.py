def cube_odd(arr):
    x = [i for i in arr if not isinstance(i, bool)]
    if len(x) == len(arr):
        try:
            return sum([i ** 3 for i in x if i % 2])
        except:
            pass
