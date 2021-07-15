def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    import math
    a = [age_1, age_2,age_3, age_4, age_5, age_6, age_7, age_8 ]
    b= []
    for x in a:
        b.append(x*x)
    
    s = sum(b)
    
    s = math.sqrt(s)
    
    s = s/2
    return int(s)
