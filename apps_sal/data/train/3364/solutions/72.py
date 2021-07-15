def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    a = (age_1 * age_1) + (age_2 * age_2) + (age_3 * age_3) + (age_4 * age_4) + (age_5 * age_5) + (age_6 * age_6) + (age_7 * age_7) + (age_8 * age_8)
    b = a**.5
    return int(b // 2)
