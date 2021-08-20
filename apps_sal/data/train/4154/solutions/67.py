def is_triangle(a, b, c):
    my_flag = False
    if a + b > c and c + b > a and (a + c > b):
        my_flag = True
    else:
        my_flag = False
    return my_flag
