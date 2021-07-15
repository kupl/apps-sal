def is_triangle(a, b, c):
    if (abs(b-a)<c<abs(b+a) and
       abs(c-a)<b<abs(c+a) and
       abs(c-b)<a<abs(c+b)):
           return True
    return False

