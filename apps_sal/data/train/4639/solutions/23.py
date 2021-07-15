def power_of_two(x):
    n, t = 0, 0
    while t < x:
        t = 2**n
        if t == x: return True
        n += 1
    return False 
