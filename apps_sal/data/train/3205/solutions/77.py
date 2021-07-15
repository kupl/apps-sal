def is_divisible(n,x,y):
    quotient_nx = n%x
    quotient_ny= n%y
    if quotient_nx == 0 and quotient_ny == 0:
        return True
    else:
        return False

