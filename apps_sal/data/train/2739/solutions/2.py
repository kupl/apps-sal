def cube_odd(arr):
    if len(set(map(type,arr))) < 2:
        return sum(n**3 for n in arr if n%2)
