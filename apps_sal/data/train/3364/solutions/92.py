import math
def predict_age(a1, a2, a3, a4, a5, a6, a7, a8):
    array= [a1,a2,a3,a4,a5,a6,a7,a8]
    return int(math.sqrt(sum(x**2 for x in array))/2)
