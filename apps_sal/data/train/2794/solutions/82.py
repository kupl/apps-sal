def calculate_age(b, c):
    d=c-b
    return  (d>0)  * f"You are {d} year{'s'*(d>1)} old." +\
            (d<0)  * f"You will be born in {-d} year{'s'*(d<-1)}." +\
            (d==0) * "You were born this very year!"
