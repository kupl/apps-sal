import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    all_ages = []
    all_ages.extend([age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8])
    x = 0
    for age in all_ages:
        age = age * age
        x += age
    y = math.sqrt(x)
    return int(y / 2)
