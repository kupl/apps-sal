import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age_1 *= age_1
    age_2 *= age_2
    age_3 *= age_3
    age_4 *= age_4
    age_5 *= age_5
    age_6 *= age_6
    age_7 *= age_7
    age_8 *= age_8

    age = age_1 + age_2 + age_3 + age_4 + age_5 + age_6 + age_7 + age_8
    return math.floor(math.sqrt(age)/2)
