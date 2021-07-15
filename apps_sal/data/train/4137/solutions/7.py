from math import sqrt
def is_square(n):  
    if n<0:
        return False
    count=0
    m=int(sqrt(n))
    if m*m==n:
        count=1
    if count==1:
        return True
    else :
        return False
