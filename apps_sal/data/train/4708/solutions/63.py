def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    for y in range(0,human_years):
        if y == 0:
            cat_years += 15
            dog_years += 15
        elif y == 1:
            cat_years += 9
            dog_years += 9
        else:
            cat_years += 4
            dog_years += 5
    return [human_years,cat_years,dog_years]
