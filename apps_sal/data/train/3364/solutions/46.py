def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    
    new_ages = []
    
    for i in ages:
        x = i * i
        new_ages.append(x)
        
    step3 = sum(new_ages)
    step4 = (step3 ** (1/2))
    step5 = (step4 // 2)
    return step5
