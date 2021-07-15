def roots(a,b,c):
    # your code
    D = b**2-4*a*c
    if D<0:
        #No solution in the set of real numbers
        return None
    if D==0:
        #Same "double" solution
        x= (-b+D**0.5)/(2*a)
        return round(x*2,2)
    if D>0:
        #Two different solutions
        x1 = (-b+D**0.5)/(2*a)
        x2 = (-b-D**0.5)/(2*a)
        return round((x1+x2),2)
