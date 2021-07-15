def is_triangle(a, b, c):
    result = False
    if a + b > c:
        if a + c > b:
            if c + b > a:
                result = True  
    return result

