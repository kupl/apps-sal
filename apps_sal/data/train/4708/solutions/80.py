def human_years_cat_years_dog_years(human_years):
    years = [0, 0, 0]
    for i in range(0, human_years):
        if years[0] == 0:
            years[0] += 1
            years[1] += 15
            years[2] += 15
        elif years[0] == 1:
            years[0] += 1
            years[1] += 9
            years[2] += 9
        else:
            years[0] += 1
            years[1] += 4
            years[2] += 5
    return years
