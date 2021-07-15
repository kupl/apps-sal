def is_triangle(a, b, c):
    cond1 = a + b > c
    cond2 = b + c > a 
    cond3 = a + c > b
    list = [cond1, cond2, cond3]
    if False in list:
        return False
    return True
