def cube_odd(arr):
    func = lambda x: isinstance(x, (int,float)) and not isinstance(x, bool)
    return (all(map(func,arr)) or None) and sum(x**3 for x in arr if x**3%2)
