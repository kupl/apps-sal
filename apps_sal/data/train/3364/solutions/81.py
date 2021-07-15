import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age_1 = age_1 * age_1
    age_2 = age_2 * age_2
    age_3 = age_3 * age_3
    age_4 = age_4 * age_4
    age_5 = age_5 * age_5
    age_6 = age_6 * age_6
    age_7 = age_7 * age_7
    age_8 = age_8 * age_8
    output = age_1 + age_2 + age_3 + age_4 + age_5 + age_6 + age_7 + age_8
    output = math.sqrt(output)
    a = output // 2
    return math.floor(a)

