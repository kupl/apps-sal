import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    return math.sqrt(sum([x**2 for x in age])) // 2
