def cube_odd(arr):
    if all((type(x) is int or type(x) is float for x in arr)):
        return sum((x ** 3 for x in arr if x % 2))
