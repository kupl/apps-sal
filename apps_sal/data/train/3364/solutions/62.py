import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age1 = age_1 ** 2
    age2 = age_2 ** 2
    age3 = age_3 ** 2
    age4 = age_4 ** 2
    age5 = age_5 ** 2
    age6 = age_6 ** 2
    age7 = age_7 ** 2
    age8 = age_8 ** 2
    sumofages = age1 + age2+ age3+ age4+ age5+ age6+ age7+ age8
    sqrtofage = sumofages ** 0.5
    final = sqrtofage / 2
    return math.floor(final)


