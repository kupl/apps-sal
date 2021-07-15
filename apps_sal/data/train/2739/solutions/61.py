def cube_odd(arr):
    _arr = [n for n in arr if type(n) == int]
    if len(_arr) != len(arr):
        return None
    arr = [n ** 3 for n in arr if n % 2 != 0]
    return 0 if not arr else sum(arr)
