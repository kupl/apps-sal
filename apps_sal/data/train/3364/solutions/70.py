import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    
    z = []
    z.append(age_1)
    z.append(age_2)
    z.append(age_3)
    z.append(age_4)
    z.append(age_5)
    z.append(age_6)
    z.append(age_7)
    z.append(age_8)
    
    y = []
    
    for i in z:
        y.append(i*i)
        
    x = sum(y)
    
    x = math.sqrt(x)
    
    return (x//2)
