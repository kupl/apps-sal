from math import sqrt


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    age2 = []
    age3 = 0
    for i in age:
        age2.append(i * i)
    for i in age2:
        age3 += i
    return int(sqrt(age3) / 2)
