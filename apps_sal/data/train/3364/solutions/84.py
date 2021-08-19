import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    list = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    squared_list = [a ** 2 for a in list]
    added_squared_list = math.sqrt(sum(squared_list)) / 2
    return int(added_squared_list)
