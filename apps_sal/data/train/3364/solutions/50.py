def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    arr = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    return sum([el*el for el in arr]) ** 0.5 // 2

