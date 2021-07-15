def is_triangle(a, b, c):
    s=[a,b,c]
    for i in s:
        if sum(s)-i <= i:
            return False
    return True
