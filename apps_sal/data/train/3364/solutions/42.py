import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    list = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    sum = 0
    for i in list:
        sum += i * i

    return math.floor(math.sqrt(sum) / 2)
