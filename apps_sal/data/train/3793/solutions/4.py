# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    a, b, c = sorted([a, b, c])
    if a + b <= c:
        return 0
    elif a**2 + b**2 > c**2:
        return 1
    elif a**2 + b**2 == c**2:
        return 2
    else:
        return 3
