from math import floor
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    return floor((sum(i**2 for i in age))**0.5/2)
