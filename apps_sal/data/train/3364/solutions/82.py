def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    starting_list = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    each_muliply_itself = []
    for age in starting_list:
        each_muliply_itself.append(age * age)
    total_multiplied_ages = sum(each_muliply_itself)
    square_root_result = total_multiplied_ages ** 0.5
    result = square_root_result / 2
    return int(result)
