def solve_eq(eq):
    d = det(eq[0][0], eq[0][1], eq[0][2], eq[1][0], eq[1][1], eq[1][2], eq[2][0], eq[2][1], eq[2][2])
    return [det(eq[0][3], eq[0][1], eq[0][2], eq[1][3], eq[1][1], eq[1][2], eq[2][3], eq[2][1], eq[2][2])/d, det(eq[0][0], eq[0][3], eq[0][2], eq[1][0], eq[1][3], eq[1][2], eq[2][0], eq[2][3], eq[2][2])/d, det(eq[0][0], eq[0][1], eq[0][3], eq[1][0], eq[1][1], eq[1][3], eq[2][0], eq[2][1], eq[2][3])/d]   
    
def det(a, b, c, d, e,f, g, h, i):
    return int(a * (e * i - h * f) - b * (d * i - g * f) + c * (d * h - g * e))
    
    
    
    


