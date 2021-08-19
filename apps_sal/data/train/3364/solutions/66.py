def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    li = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    b = [x ** 2 for x in li]
    return int(sum(b) ** 0.5 / 2)
