import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    ages1 = []
    for age in ages:
        age *= age
        ages1.append(age)
    age_sm = sum(ages1)
    return math.floor(math.sqrt(age_sm) / 2)
