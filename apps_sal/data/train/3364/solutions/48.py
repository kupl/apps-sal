import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages = (age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8)
    suma = 0 
    result = 0
    for age in ages:
        suma += age * age
    result = (math.sqrt(suma)) // 2
    return result
