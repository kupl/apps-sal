import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    i = 0
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    for j in ages:
        ages[i] = j**2
        i += 1
    return math.sqrt(sum(ages)) // 2
