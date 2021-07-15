def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):

    l = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    m = int((sum([i * i for i in l]) ** 0.5) /2)
    return m
    

print((predict_age(65, 60, 75, 55, 60, 63, 64, 45)))

    
    

