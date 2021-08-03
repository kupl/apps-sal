def is_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        result = True
        print(result)
    else:
        result = False
        print(result)
    return result
