def solve_for_x(s):    
    for i in range(-1000, 1000):
        if eval(s.replace('x', str(i)).replace('=', '==')):
            return i
