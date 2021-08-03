from math import sqrt


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    s = sum([x * x for x in [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]])
    return sqrt(s) // 2
