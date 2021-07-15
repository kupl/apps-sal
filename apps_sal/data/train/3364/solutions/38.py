import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    result = 0
    result += age_1 * age_1
    result += age_2 * age_2
    result += age_3 * age_3
    result += age_4 * age_4
    result += age_5 * age_5
    result += age_6 * age_6
    result += age_7 * age_7
    result += age_8 * age_8
    result = math.sqrt(result)
    result = result/2    
    
    return int(result)
