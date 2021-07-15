def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    total = 0

    for i in range(0,len(age)):
        multi_itself = age[i] * age[i]
        total = total + multi_itself

    square_root = pow(total, 0.5)
    return int(square_root / 2)
