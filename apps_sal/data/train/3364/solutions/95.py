import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ls = age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8
    return int(math.sqrt(sum([num*num for num in ls])) / 2)

