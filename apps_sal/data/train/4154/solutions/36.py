def is_triangle(a, b, c):
    if a == None or b == None or c == None:
        return False
    l_tri = sorted([a,b,c])
    if l_tri[2]>=l_tri[0]+l_tri[1]:
        return False
    return True

