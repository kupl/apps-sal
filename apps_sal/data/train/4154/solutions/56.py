def is_triangle(a, b, c):
    if a+b>c and abs(a-b)<c:
        return True
    elif a+c>b and abs(a-c)<b:
        return True
    elif b+c>a and abs(b-c)<a:
        return True
    else:
    
        return False

