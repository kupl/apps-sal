import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    new_list = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]

    mult_list = math.sqrt(sum([i**2 for i in new_list])) // 2

    return mult_list
