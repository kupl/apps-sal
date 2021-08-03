def is_triangle(a, b, c):
    if(abs(a + b) <= c or abs(a - b) >= c):
        return False
    elif(abs(c + b) <= a or abs(c - b) >= a):
        return False
    elif(abs(c + a) <= b or abs(c - a) >= b):
        return False
    elif(a <= 0 or b <= 0 or c <= 0):
        return False
    return True
