def human_years_cat_years_dog_years(human_years):
    ages = [0, 0, 0]
    if human_years == 1:
        ages[0] = 1
        ages[1] = 15
        ages[2] = 15
    if human_years == 2:
        ages[0] = 2
        ages[1] = 24
        ages[2] = 24
    if human_years >= 3:
        ages[0] = human_years
        ages[1] = 24 + (human_years - 2) * 4
        ages[2] = 24 + (human_years - 2) * 5
    return ages
