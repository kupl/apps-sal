def is_triangle(a, b, c):
    if a==0 or b==0 or c==0:
        return 0
    if a+b<=c or b+c<=a or a+c<=b:
        return 0
    else:
        return 1

