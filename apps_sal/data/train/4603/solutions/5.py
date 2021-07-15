def Ackermann(m,n):
    if type(m) != int or type(n) != int or m < 0 or n < 0:
        return None
    else:
        if m == 0:
            return n+1
        elif n == 0:
            return Ackermann(m-1,1)
        else:
            return Ackermann(m-1,Ackermann(m,n-1))
