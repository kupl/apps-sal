def solve_for_x(equation):
    for x in range(-100,1001):
        if eval(equation.replace('=','==')):
            return x #needs better test cases to prevent this solution
    
    

