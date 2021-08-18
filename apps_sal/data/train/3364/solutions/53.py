import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    list = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    grand_secret = 0
    for age in list:
        grand_secret = grand_secret + (age**2)
    grand_secret = math.sqrt(grand_secret)
    grand_secret = grand_secret / 2
    return int(grand_secret)
