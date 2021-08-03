def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age_multiplied_and_added = age_1 ** 2 + age_2 ** 2 + age_3 ** 2 + age_4 ** 2 + age_5 ** 2 + age_6 ** 2 + age_7 ** 2 + age_8 ** 2
    age_multiplied_and_added_and_squared = age_multiplied_and_added ** 0.5
    return int(age_multiplied_and_added_and_squared / 2)
