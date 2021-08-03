def cube_odd(arr):
    res = 0
    for n in arr:
        if type(n) != int:
            return None
        res += n**3 if n % 2 else 0
    return res
