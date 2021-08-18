def human_years_cat_years_dog_years(human_years):
    caty = 0
    for i in range(0, human_years):
        if i == 0:
            caty += 15
        elif i == 1:
            caty += 9
        else:
            caty += 4
    dogy = 0
    for i in range(0, human_years):
        if i == 0:
            dogy += 15
        elif i == 1:
            dogy += 9
        else:
            dogy += 5

    return [human_years, caty, dogy]
