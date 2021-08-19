def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    # your
    sum = 0
    # calculate sum of ages
    sum += age_1**2 + age_2**2 + age_3**2 + age_4**2 + age_5**2 + age_6**2 + age_7**2 + age_8**2

    # square root and divide by 2
    return (sum**0.5) // 2
