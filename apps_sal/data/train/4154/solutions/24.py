def is_triangle(a, b, c):
    t1 = a + b > c
    t2 = a + c > b
    t3 = b + c > a

    return t1 and t2 and t3
    # return False
