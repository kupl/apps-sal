import math 
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    k=age_1**2
    n=age_2**2
    g=age_3**2
    l=age_4**2
    t=age_5**2
    j=age_6**2
    i=age_7**2
    e=age_8**2
    b=k+n+g+l+t+j+i+e
    return math.sqrt(b)//2
