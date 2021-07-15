from math import *
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    a = age_1*age_1
    b = age_2*age_2
    c = age_3*age_3
    d = age_4*age_4
    e = age_5*age_5
    f = age_6*age_6
    g = age_7*age_7
    h = age_8*age_8
    i = a+b+c+d+e+f+g+h
    j = sqrt(i)
    h = floor(j/2)
    return h
