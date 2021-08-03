def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    value = 0
    for age in ages:
        sqw = age * age
        value += sqw
    value = value ** 0.5
    value = int(value // 2)
    return value
