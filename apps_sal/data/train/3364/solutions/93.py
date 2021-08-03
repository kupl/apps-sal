def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    sum_ages = 0
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    for x in ages:
        sum_ages += x**2
    swaureroot = sum_ages**(1 / 2)
    return int(swaureroot / 2)
